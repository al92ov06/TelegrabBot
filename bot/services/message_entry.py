from datetime import datetime
import pytz


# Запись полученных сообщений от webhook в файл
class MessageRecoding:
    def __init__(self, data):
        self.data = data

    def message_entry_tg(self):
        with open('bot/logs/messages_tg.txt', 'a') as file:
            time_moscow = datetime.now(pytz.timezone('Europe/Moscow'))
            cat_id = self.data['message']['chat']['id']
            text = self.data['message']['text']
            message_str = f'[{time_moscow}] --- user_id: {cat_id}, text: {text};\n {self.data}'
            file.write(message_str + '\n')

    def message_entry_whatsapp(self):
        pass
