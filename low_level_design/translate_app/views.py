# translate_app/views.py
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import TranslationJob
from .serializers import (
    TranslationJobCreateSerializer,
    TranslationJobStatusSerializer,
    TranslationJobResultSerializer,
)
from .tasks import enqueue_translation_job


# --- Create a Translation Job (User only)
class TranslationCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TranslationJobCreateSerializer
    queryset = TranslationJob.objects.all()

    def perform_create(self, serializer):
        job = serializer.save(user=self.request.user)
        enqueue_translation_job.delay(str(job.id))  # Celery async
        return job


# --- Get Job Status
class TranslationStatusView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TranslationJobStatusSerializer
    queryset = TranslationJob.objects.all()
    lookup_field = 'id'


# --- Get Translated Result
class TranslationResultView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TranslationJobResultSerializer
    queryset = TranslationJob.objects.all()
    lookup_field = 'id'


# --- Get All Jobs (Admin only)
class TranslationListAllView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TranslationJobStatusSerializer
    queryset = TranslationJob.objects.all().order_by('-created_at')


# --- Admin or Worker updates job status
@api_view(["PATCH"])
@permission_classes([permissions.IsAdminUser])
def admin_update_job_status(request, id):
    job = get_object_or_404(TranslationJob, id=id)
    new_status = request.data.get("status")

    if new_status not in dict(TranslationJob.STATUS_CHOICES).keys():
        return Response({"error": "Invalid status value"}, status=status.HTTP_400_BAD_REQUEST)

    job.status = new_status
    if new_status == "in_progress":
        job.mark_started()
    elif new_status == "completed":
        job.mark_completed()

    job.save()
    return Response({"message": f"Job status updated to {new_status}"}, status=status.HTTP_200_OK)
