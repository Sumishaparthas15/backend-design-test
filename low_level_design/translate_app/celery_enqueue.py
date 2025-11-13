# translate_app/tasks.py (add)
@shared_task
def enqueue_translation_job(job_id):
    job = TranslationJob.objects.get(id=job_id)
    if job.priority in ['urgent', 'high']:
        process_translation.apply_async(args=[str(job.id)], queue='translation_high_priority')
    else:
        process_translation.apply_async(args=[str(job.id)], queue='translation_normal')
