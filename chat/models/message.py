from django.contrib.auth import get_user_model
from django.db import models

from chat.models.abstract_model import AbstractModel


class Message(AbstractModel):
    class Meta:
        db_table = "message"
        verbose_name = "メッセージ"
        verbose_name_plural = "メッセージ"

    id = models.AutoField(primary_key=True,
                          unique=True,
                          serialize=True,
                          auto_created=True)
    message = models.TextField(max_length=500)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET(0))
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    @staticmethod
    def create_message(message_text, user_id, room_id):
        message = Message(message=message_text, user_id=user_id, room_id=room_id)
        message.save()
        return message

    @classmethod
    def index_messages(cls, room_id=1):
        return Message.objects.filter(room_id=room_id).order_by("created_at").reverse()[0:100]
