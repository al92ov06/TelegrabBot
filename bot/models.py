from django.db import models

# Необходимо полностью адаптировать бота для работы через бд
# (авторизация, запись сообщений, полученных данных от Yandex direct)
"""
class Users(models.Model):
    user_id = models.BigAutoField()
    username = models.CharField(max_length=35, help_text="Введите имя nickname")
    last_name = models.CharField(max_length=35, help_text="Введите фамилию пользователя")
    first_name = models.CharField(max_length=35, help_text="Введите имя пользователя")
    language_code = models.CharField(max_length=5)
    creation_date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True)
    permission_answer = models.BooleanField()
"""


# Запись Token Yandex Direct чтобы не хранить в коде
class AccountYandexDirect(models.Model):
    token_yandex_direct = models.TextField()
    login_yandex_direct = models.CharField(max_length=35)
    account_name = models.CharField(max_length=35, help_text="Введите название аккаунта")


# Запись Token Telebot чтобы не хранить в коде
class BotData(models.Model):
    messengers_name = models.CharField(max_length=35, help_text="введите название мессанджера ")
    bot_username = models.CharField(max_length=35, help_text="введите имя бота ")
    token_bot = models.TextField()
