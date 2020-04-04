from django.urls import path

from chat.views import index, chat_sample

urlpatterns = [
    path("", index),
    path("<int:room_id>/", chat_sample),
]
