from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bot.telegram_bot.send_messages import *
from bot.services.message_entry import MessageRecoding
from bot.repository.logs_in import bot_token, yandex_direct_token


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        r = json.loads(request.body)
        m = SendMessage(r)
        m.send_message()
        d = MessageRecoding(r)
        d.message_entry_tg()

    return HttpResponse("<h1>Что за чудный бот</h1>")


def test(request):
    token = yandex_direct_token()
    return HttpResponse(f"<h1>{token}</h1>")
