import telebot

from bot.data_analysis.analyses_click_fraud import AnalysesClickFraud
from bot.services.message_preparation import MessagePreparation
from bot.services.entry_to_file import campaign_entry_stop
from bot.telegram_bot.menu import menu
from bot.telegram_bot.messages_report import messages_report
from bot.yandex_direct.get_data import GetData
from bot.repository.logs_in import bot_token


# Класс для отправки сообщений в telegram
class SendMessage:

    def __init__(self, message):
        token = bot_token()
        self.bot = telebot.TeleBot(token)
        object = MessagePreparation(message)
        self.message = object.preparation_tg_message()

    def send_message(self):
        if self.message['text'] == '/help' or self.message['text'] == '/start':
            self.__send_answer_to_help()
        elif self.message['text'] == '/balance':
            self.__send_answer_to_balance()
        elif self.message['text'] == '/report_month':
            self.__send_answer_to_report_mouth()
        elif self.message['text'] == '/report_day':
            self.__send_answer_to_report_day()
        elif self.message['text'] == '/analyze_on':
            self.__send_answer_to_analyze()
        elif self.message['text'] == '/get_list_stop':
            self.__send_answer_to_get_list_stop()
        elif self.message['text'] == '/analyze_off':
            self.__send_answer_to_analyze_off()
        elif self.message['text'] == '/stop':
            self.__send_answer_to_stop()
        else:
            self.__send_answer_to_help()

    def __send_answer_to_help(self):
        menus = menu()
        self.bot.send_message(self.message['cat_id'], '\n'.join(menus), parse_mode="HTML")

    def __send_answer_to_balance(self):
        object = GetData()
        balance = object.get_balance()
        self.bot.send_message(self.message['cat_id'], f'<b>Баланс:</b>\n{balance}', parse_mode="HTML")

    def __send_answer_to_report_mouth(self):
        obj = GetData()
        date = obj.get_reports(data_range='THIS_MONTH', name_reports='MON')
        text = messages_report(date)
        with open('reports.txt', 'w') as file:
            text = '\n'.join(text)
            file.write(text + '\n')
        f = open('reports.txt', 'rb')
        self.bot.send_document(self.message['cat_id'], f'<b>Список кампаний на остановку:</b>\n{f}')

    def __send_answer_to_report_day(self):
        obj = GetData()
        date = obj.get_reports(data_range='TODAY', name_reports='TOD')
        text = messages_report(date)
        text = '\n'.join(text)
        self.bot.send_message(self.message['cat_id'], text, parse_mode="HTML")

    def __send_answer_to_analyze(self):
        obj = AnalysesClickFraud()
        text = obj.click_fraud()
        campaign_entry_stop(text)
        if len(text) == 0:
            mes = 'Все ок!'
        else:
            mes = '<b>Список капаний на остановку:</b>\n' + '\n'.join(text)
        self.bot.send_message(self.message['cat_id'], mes, parse_mode="HTML")

    def __send_answer_to_get_list_stop(self):
        with open('bot/logs/list_stop_campaign.txt') as file:
            f = file.read()
            self.bot.send_message(self.message['cat_id'], f'<b>Список капаний на остановку:</b>\n{f}',
                                  parse_mode="HTML")

    def __send_answer_to_analyze_off(self):
        self.bot.send_message(self.message['cat_id'], 'Автоматический анализ отключен!')

    def __send_answer_to_stop(self):
        self.bot.send_message(self.message['cat_id'], 'Функция отключена для безопасности.')
