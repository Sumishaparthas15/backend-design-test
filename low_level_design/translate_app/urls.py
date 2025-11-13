# translate_app/urls.py
from django.urls import path
from .views import TranslationCreateView, TranslationStatusView, TranslationResultView

urlpatterns = [
    path('translate/', TranslationCreateView.as_view(), name='translate-create'),
    path('translate/<uuid:id>/status/', TranslationStatusView.as_view(), name='translate-status'),
    path('translate/<uuid:id>/result/', TranslationResultView.as_view(), name='translate-result'),
]
