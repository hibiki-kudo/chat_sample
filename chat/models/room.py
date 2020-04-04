from django.db import models

from chat.models.abstract_model import AbstractModel


class Room(AbstractModel):
    class Meta:
        db_table = "room"
        verbose_name = "チャットルーム"
        verbose_name_plural = "チャットルーム"

    id = models.AutoField(primary_key=True,
                          unique=True,
                          serialize=True,
                          auto_created=True)

    @staticmethod
    def find_by(room_id):
        return Room.objects.get(id=room_id)
