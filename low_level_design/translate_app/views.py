# translate_app/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import TranslationJob
from .serializers import TranslationJobCreateSerializer, TranslationJobStatusSerializer, TranslationJobResultSerializer
from .tasks import enqueue_translation_job

from django.shortcuts import get_object_or_404

class TranslationCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TranslationJobCreateSerializer
    queryset = TranslationJob.objects.all()

    def perform_create(self, serializer):
        job = serializer.save(user=self.request.user)
        # Enqueue task: chooses queue based on job.priority
        enqueue_translation_job.delay(str(job.id))

class TranslationStatusView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TranslationJobStatusSerializer
    queryset = TranslationJob.objects.all()
    lookup_field = 'id'

class TranslationResultView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TranslationJobResultSerializer
    queryset = TranslationJob.objects.all()
    lookup_field = 'id'
