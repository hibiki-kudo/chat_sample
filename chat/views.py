from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from chat.models.message import Message
from chat.models.room import Room


def index(request):
    messages = Message.index_messages()
    return render(request, "chat/index.html", context={"messages": messages})


def chat_sample(request, room_id):
    room = Room.find_by(room_id)
    return render(request, 'chat/chat_sample.html', {
        'room_name': room.id,
        'messages': Message.index_messages(room.id)
    })


def success_response_format(params):
    return {
        "status": "success",
        "status_code": 200,
        "detail": {**params}
    }


@require_http_methods(["GET"])
def index_messages(request, room_id):
    messages = Message.index_messages(room_id)
    return JsonResponse(success_response_format(messages))
