from django.contrib import admin

from chat.models.message import Message
from chat.models.room import Room

admin.site.register(Message)
admin.site.register(Room)
