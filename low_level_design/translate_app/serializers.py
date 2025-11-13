# translate_app/serializers.py
from rest_framework import serializers
from .models import TranslationJob

class TranslationJobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationJob
        fields = ['id', 'source_text', 'source_lang', 'target_lang', 'priority']

    def validate(self, data):
        if not data.get('source_text'):
            raise serializers.ValidationError("Source text is required.")
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
        fields = ['id', 'status', 'translated_text', 'error_message']

class TranslationJobAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationJob
        fields = [
            'id',
            'user',
            'source_text',
            'translated_text',
            'source_lang',
            'target_lang',
            'status',
            'priority',
            'word_count',
            'error_message',
            'created_at',
            'started_at',
            'completed_at',
        ]
