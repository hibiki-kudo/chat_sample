from django.urls import path
from push_notifications.api.rest_framework import WebPushDeviceViewSet

from chat.views import index, chat_sample

urlpatterns = [
    path("", index),
    path("web_push/", WebPushDeviceViewSet),
    path("<int:room_id>/", chat_sample),
]
