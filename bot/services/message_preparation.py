# Подготовка запроса с webhook для отправки сообщения
class MessagePreparation:
    def __init__(self, data_query):
        self.data_query = data_query

    # Подготовка данных для отправки в телеграм
    def preparation_tg_message(self) -> dict:
        cat_id = self.data_query['message']['chat']['id']
        text = self.data_query['message']['text']
        return {'cat_id': cat_id, 'text': text}

    # Подготовка данных для отправки в whatsapp
    def preparation_whatsapp_message(self):
        pass
