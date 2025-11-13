# Pseudocode for translation processing and autoscaling

## Worker enqueue logic (called by API create endpoint)
function enqueue_translation_job(job_id):
    job = db.get_translation_job(job_id)
    if job.priority == "urgent":
        queue_name = "urgent_queue"
    elif job.priority == "high":
        queue_name = "high_queue"
    else:
        queue_name = "default_queue"
    push_to_queue(queue_name, job_id)
    db.insert_translation_queue(job_id, queue_name)

## Worker processing (single worker)
function worker_consume(queue_name):
    while true:
        job_id = queue.pop(queue_name)  # blocking receive
        if job_id is None:
            continue
        job = db.get_translation_job(job_id)
        job.mark_started()  # sets status & started_at
        try:
            # Option A: call external service (Google/AWS/OpenAI)
            translated_text = call_external_translator(job.source_text, job.source_lang, job.target_lang)
            job.translated_text = translated_text
            job.mark_completed()
            db.update_job(job)
            db.set_queue_processed(job_id)
        except TransientError as e:
            # retry logic, exponential backoff (or use Celery retries)
            requeue(job_id)  # or rely on Celery retries
        except Exception as e:
            job.status = "failed"
            job.error_message = str(e)
            db.update_job(job)

## Autoscaler (controller runs periodically)
function autoscaler_loop():
    while true:
        metrics = get_metrics()  # queue lengths, worker count, CPU usage
        pending = metrics.queue_length_total  # sum across queues
        workers = metrics.active_workers

        # scale up rules
        if pending > workers * 10 and workers < MAX_WORKERS:
            spawn_instances = min(MAX_WORKERS - workers, ceil((pending / 10) - workers))
            spawn_new_workers(spawn_instances)

        # scale down rules (graceful)
        if pending == 0 and workers > MIN_WORKERS:
            idle_workers = get_idle_worker_count()
            if idle_workers > 0:
                terminate_workers(min(idle_workers, workers - MIN_WORKERS))

        sleep(POLL_INTERVAL_SECONDS)
