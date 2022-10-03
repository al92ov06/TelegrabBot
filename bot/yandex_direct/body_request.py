# Класс содержит методы с headers и body для отправки запроса Yandex API
# Метод get_costs - получение отчета "Расходы". Принимает флаг если True отчет за текущий месяц, если False за день
# Метод get_balance - получение "Баланса"
# Метод suspend - запрос на остановку РК (всех РК). Принимает строку с id РК (разделитель ",")
# Метод get_id_companings_status_on() - получение списка "Запущенные кампании"
from bot.repository.logs_in import yandex_direct_token


class BodyRequest:
    # OAuth-токен пользователя, от имени которого будут выполняться запросы
    __token = yandex_direct_token()
    __api_url = 'https://api.direct.yandex.com/'

    # data_range = THIS_MONTH | TODAY
    def get_reports(self, data_range='THIS_MONTH', name_report='mo') -> dict:
        # Адрес сервиса Reports для отправки JSON-запросов (регистрозависимый)
        reports_url = f'{self.__api_url}json/v5/reports'
        # --- Подготовка запроса ---
        # Создание HTTP-заголовков запроса
        headers = {
            # OAuth-токен. Использование слова Bearer обязательно
            "Authorization": "Bearer " + self.__token,
            # Язык ответных сообщений
            "Accept-Language": "ru",
            # Режим формирования отчета
            "processingMode": "auto",
            # Выводить расходы с точностью до 2-х знаков после запятой
            "returnMoneyInMicros": "false",
            # Не выводить в отчете строку с количеством строк статистики
            "skipReportSummary": "true"
        }
        # Создание тела запроса
        body = {
            "params": {
                "SelectionCriteria": {
                },
                "FieldNames": [
                    "Date",
                    'CampaignId',
                    "CampaignName",
                    "Impressions",
                    "Ctr",
                    'Conversions',
                    "Clicks",
                    "Cost"
                ],
                "ReportName": (f"НАЗВАНИЕ_ОТЧЕТА-{name_report}"),
                "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
                "DateRangeType": data_range,
                "Format": "TSV",
                "IncludeVAT": "YES",
                "IncludeDiscount": "NO"
            }
        }

        result = {'body': body, 'headers': headers, 'ReportsURL': reports_url}
        return result

    def get_balance(self) -> dict:
        # --- Входные данные ---
        # Адрес сервиса Reports для отправки JSON-запросов (регистрозависимый)
        reports_url = f'{self.__api_url}live/v4/json/'

        # --- Подготовка запроса ---
        # Создание HTTP-заголовков запроса
        headers = {
            # OAuth-токен. Использование слова Bearer обязательно
            "Authorization": "Bearer " + self.__token,
            # Язык ответных сообщений
            "Accept-Language": "ru",
            # Режим формирования отчета
            "processingMode": "auto",
            # Выводить расходы с точностью до 2-х знаков после запятой
            "returnMoneyInMicros": "false",
        }

        # Создание тела запроса
        body = {
            "method": "AccountManagement",
            "token": self.__token,
            "param": {
                "Action": "Get",
                "SelectionCriteria": {
                },
            },
            'locale': "ru",
        }

        result = {'body': body, 'headers': headers, 'ReportsURL': reports_url}
        return result

    # Метод suspend - запрос на остановку РК (всех РК). Принимает строку с id РК (разделитель ",")

    def suspend(self, companing_id_list: list) -> dict:
        # --- Входные данные ---
        # Адрес сервиса Reports для отправки JSON-запросов (регистрозависимый)
        reports_url = f'{self.__api_url}json/v5/campaigns'

        # --- Подготовка запроса ---
        # Создание HTTP-заголовков запроса
        headers = {
            # OAuth-токен. Использование слова Bearer обязательно
            "Authorization": "Bearer " + self.__token,
            # Язык ответных сообщений
            "Accept-Language": "ru",
            # Режим формирования отчета
            "processingMode": "auto",
            # Выводить расходы с точностью до 2-х знаков после запятой
            "returnMoneyInMicros": "false",
        }

        # Создание тела запроса
        body = {
            "method": "suspend",
            "params": {
                "SelectionCriteria": {
                    "Ids": companing_id_list
                }
            }
        }

        result = {'body': body, 'headers': headers, 'ReportsURL': reports_url}
        return result

    def get_id_companings_status_on(self):
        # --- Входные данные ---
        # Адрес сервиса Reports для отправки JSON-запросов (регистрозависимый)
        reports_url = f'{self.__api_url}json/v5/campaigns'

        # --- Подготовка запроса ---
        # Создание HTTP-заголовков запроса
        headers = {
            # OAuth-токен. Использование слова Bearer обязательно
            "Authorization": "Bearer " + self.__token,
            # Язык ответных сообщений
            "Accept-Language": "ru",
            # Режим формирования отчета
            "processingMode": "auto",
            # Выводить расходы с точностью до 2-х знаков после запятой
            "returnMoneyInMicros": "false",
        }

        # Создание тела запроса
        body = {
            "method": "get",
            "params": {
                "SelectionCriteria": {
                    "States": ['ON', 'OFF'],
                },
                "FieldNames": ["Id", "Name"]
            }
        }

        result = {'body': body, 'headers': headers, 'ReportsURL': reports_url}
        return result
