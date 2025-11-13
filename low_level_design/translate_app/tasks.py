import httpx
from celery import shared_task
from django.utils import timezone
from .models import TranslationJob


@shared_task
def enqueue_translation_job(job_id):
    """
    Celery task to translate text using MyMemory API (synchronous).
    Automatically updates job status and translated text.
    """
    try:
        job = TranslationJob.objects.get(id=job_id)
        job.status = "in_progress"
        job.started_at = timezone.now()
        job.save()

        # Use normal httpx.get (NOT async)
        url = "https://api.mymemory.translated.net/get"
        params = {
            "q": job.source_text,
            "langpair": f"{job.source_lang}|{job.target_lang}"
        }

        response = httpx.get(url, params=params, timeout=15)
        data = response.json()
        translated_text = data.get("responseData", {}).get("translatedText")

        if translated_text:
            job.translated_text = translated_text
            job.status = "completed"
            job.completed_at = timezone.now()
        else:
            job.status = "failed"
            job.error_message = "Translation API returned empty text."
            job.completed_at = timezone.now()

        job.save()
        return job.status

    except Exception as e:
        job.status = "failed"
        job.error_message = str(e)
        job.completed_at = timezone.now()
        job.save()
        return job.status
