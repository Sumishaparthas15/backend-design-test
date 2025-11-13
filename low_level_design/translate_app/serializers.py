# translate_app/serializers.py
from rest_framework import serializers
from .models import TranslationJob

class TranslationJobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationJob
        fields = ['id', 'source_text', 'source_file', 'source_lang', 'target_lang', 'priority']

    def validate(self, data):
        if not data.get('source_text') and not data.get('source_file'):
            raise serializers.ValidationError("Provide source_text or upload a source_file")
        if data.get('source_text'):
            wc = len(data['source_text'].split())
            data['word_count'] = wc
        return data

class TranslationJobStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationJob
        fields = ['id', 'status', 'priority', 'created_at', 'started_at', 'completed_at', 'word_count']

class TranslationJobResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationJob
        fields = ['id', 'status', 'translated_text', 'result_file']
