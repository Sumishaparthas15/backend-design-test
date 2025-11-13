# from celery import shared_task
# from django.utils import timezone
# from .models import TranslationJob
# import time
# import random
# import logging

# logger = logging.getLogger(__name__)

# # --- MOCK TRANSLATION FUNCTION ---
# def fake_translate(text, src_lang, tgt_lang):
#     """
#     Simulate translation work — replace this with a real model/API later.
#     """
#     time.sleep(random.uniform(1, 3))  # simulate processing delay
#     return f"[{tgt_lang}] " + text[::-1]  # reversed text = mock "translation"


# @shared_task
# def enqueue_translation_job(job_id):
#     """
#     Routes job to correct Celery queue based on priority.
#     """
#     try:
#         job = TranslationJob.objects.get(id=job_id)
#         queue_name = "translation_high_priority" if job.priority in ["urgent", "high"] else "translation_normal"
#         process_translation.apply_async(args=[job_id], queue=queue_name)
#         logger.info(f"Job {job_id} sent to queue: {queue_name}")
#     except TranslationJob.DoesNotExist:
#         logger.error(f"Job {job_id} not found.")


# @shared_task(bind=True)
# def process_translation(self, job_id):
#     """
#     Background task that simulates translating text or a file.
#     Updates job status and timestamps in DB.
#     """
#     try:
#         job = TranslationJob.objects.get(id=job_id)
#         job.status = "in_progress"
#         job.started_at = timezone.now()
#         job.save()

#         logger.info(f"Started translation job {job.id}")

#         # If source_text exists, translate it
#         if job.source_text:
#             translated = fake_translate(job.source_text, job.source_lang, job.target_lang)
#             job.translated_text = translated
#             job.word_count = len(job.source_text.split())

#         # If file exists, you could handle that too (mocked here)
#         elif job.source_file:
#             # In a real system, read file and translate line by line
#             job.translated_text = f"[File translated from {job.source_lang} to {job.target_lang}]"
#             job.word_count = 1000  # mock

#         time.sleep(random.uniform(1, 2))  # simulate finishing delay

#         job.status = "completed"
#         job.completed_at = timezone.now()
#         job.save()

#         logger.info(f"Completed translation job {job.id}")

#     except TranslationJob.DoesNotExist:
#         logger.error(f"Translation job {job_id} not found.")
#     except Exception as e:
#         logger.error(f"Error in job {job_id}: {e}")
#         job.status = "failed"
#         job.error_message = str(e)
#         job.save()


# # translate_app/tasks.py
# from celery import shared_task
# from .models import TranslationJob
# from django.utils import timezone
# import time
# import os
# from django.conf import settings


# def mock_translate(text, src, tgt):
#     # Mock: reverse words and add language note
#     words = text.split()
#     return f"[{src}->{tgt}] " + " ".join(reversed(words))

# @shared_task(bind=True)
# def process_translation(self, job_id):
#     try:
#         job = TranslationJob.objects.get(id=job_id)
#     except TranslationJob.DoesNotExist:
#         return {'status': 'not_found'}

#     try:
#         job.mark_started()

#         # Load source text (if file, read file)
#         if job.source_text:
#             source = job.source_text
#         elif job.source_file:
#             p = job.source_file.path
#             with open(p, 'r', encoding='utf-8', errors='ignore') as f:
#                 source = f.read()
#         else:
#             job.status = 'failed'
#             job.error_message = 'No source content'
#             job.save()
#             return {'status': 'failed'}

#         # Chunking example (simple): split into ~500-word chunks
#         words = source.split()
#         chunk_size = 500
#         chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)] or ['']

#         translated_chunks = []
#         for idx, chunk in enumerate(chunks):
#             # Simulate inference time proportional to chunk words
#             time.sleep(min(2, max(0.2, len(chunk.split())/250.0)))  # mock latency
#             translated = mock_translate(chunk, job.source_lang, job.target_lang)
#             translated_chunks.append(translated)
#             # optionally update progress (not persisted here)
#             # job.save()  # update DB periodically if needed

#         # Save result
#         job.translated_text = '\n\n'.join(translated_chunks)

#         # Optionally save to file for large outputs
#         out_name = f"{str(job.id)}_translated.txt"
#         out_path = os.path.join(settings.MEDIA_ROOT, 'translated_files', out_name)
#         os.makedirs(os.path.dirname(out_path), exist_ok=True)
#         with open(out_path, 'w', encoding='utf-8') as f:
#             f.write(job.translated_text)
#         # set result_file to relative path
#         job.result_file.name = os.path.join('translated_files', out_name)

#         job.mark_completed()
#         return {'status': 'completed'}
#     except Exception as e:
#         job.status = 'failed'
#         job.error_message = str(e)
#         job.save()
#         return {'status': 'failed', 'error': str(e)}
# translate_app/tasks.py
from celery import shared_task
from .models import TranslationJob
# ... any other imports you already have

@shared_task
def process_translation(job_id):
    # your existing translation logic
    pass


@shared_task
def enqueue_translation_job(job_id):
    from .models import TranslationJob
    job = TranslationJob.objects.get(id=job_id)
    if job.priority in ['urgent', 'high']:
        process_translation.apply_async(args=[str(job.id)], queue='translation_high_priority')
    else:
        process_translation.apply_async(args=[str(job.id)], queue='translation_normal')
