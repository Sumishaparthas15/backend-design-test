# translate_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path("translate/", TranslationCreateView.as_view(), name="translate-create"),
    path("translate/all/", TranslationListAllView.as_view(), name="translate-all"),
    path("translate/<uuid:id>/status/", TranslationStatusView.as_view(), name="translate-status"),
    path("translate/<uuid:id>/result/", TranslationResultView.as_view(), name="translate-result"),
    path("translate/<uuid:id>/admin-update/", admin_update_job_status, name="translate-admin-update"),
]
