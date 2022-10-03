from bot.models import BotData, AccountYandexDirect


def bot_token():
    bot_data = BotData.objects.get(pk=1)
    token = bot_data.token_bot
    return token

def yandex_direct_token():
    data = AccountYandexDirect.objects.get(pk=1)
    token = data.token_yandex_direct
    return token