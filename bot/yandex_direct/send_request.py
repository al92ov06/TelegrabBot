import json
from time import sleep

import requests
from requests.exceptions import ConnectionError


class SendRequest:

    def __init__(self, data_connect: dict):
        self.data_connect = data_connect

    def get_and_send_data(self) -> json:
        reports_url = self.data_connect['ReportsURL']
        body = self.data_connect['body']
        headers = self.data_connect['headers']
        body = json.dumps(body, indent=4)
        # --- Запуск цикла для выполнения запросов ---
        # Если получен HTTP-код 200, то выводится содержание отчета
        # Если получен HTTP-код 201 или 202, выполняются повторные запросы
        while True:
            try:
                req = requests.post(reports_url, body, headers=headers)
                req.encoding = 'utf-8'  # Принудительная обработка ответа в кодировке UTF-8
                if req.status_code == 400:
                    print("Параметры запроса указаны неверно или достигнут лимит отчетов в очереди")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(body))
                    print("JSON-код ответа сервера: \n{}".format(req.json()))
                    result = req.json()
                    break
                if req.status_code == 200:
                    print("Отчет создан успешно")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("Содержание отчета: \n{}".format(req.text))
                    print(req)
                    result = req.json()
                    break

                if req.status_code == 201:
                    print("Отчет успешно поставлен в очередь в режиме офлайн")
                    retry_in = int(req.headers.get("retry_in", 60))
                    print("Повторная отправка запроса через {} секунд".format(retry_in))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    sleep(retry_in)
                    continue

                if req.status_code == 202:
                    print("Отчет формируется в режиме офлайн")
                    retry_in = int(req.headers.get("retry_in", 60))
                    print("Повторная отправка запроса через {} секунд".format(retry_in))
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    sleep(retry_in)
                    continue

                if req.status_code == 500:
                    print("При формировании отчета произошла ошибка. Пожалуйста, попробуйте повторить запрос позднее")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(req.json()))
                    result = req.json()
                    break

                if req.status_code == 502:
                    print("Время формирования отчета превысило серверное ограничение.")
                    print("Пожалуйста, попробуйте изменить параметры - уменьшить период и количество данных.")
                    print("JSON-код запроса: {}".format(body))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(req.json()))
                    result = req.json()
                    break

                print("Произошла непредвиденная ошибка")
                print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                print("JSON-код запроса: {}".format(body))
                print("JSON-код ответа сервера: \n{}".format(req.json()))
                result = req.json()
                break

            # Обработка ошибки, если не удалось соединиться с сервером API Директа
            except ConnectionError:
                print("Произошла ошибка соединения с сервером API")
                result = "Произошла ошибка соединения с сервером API"
                # Принудительный выход из цикла
                break

            # Если возникла какая-либо другая ошибка
            except:
                print("Произошла непредвиденная ошибка")
                result = "Произошла непредвиденная ошибка"
                # Принудительный выход из цикла
                break
        return result

    # Метод для получения в ответ от сервера таблицы (чтобы процесс не падал)
    def get_data_table(self) -> str:
        reports_url = self.data_connect['ReportsURL']
        body = self.data_connect['body']
        headers = self.data_connect['headers']
        body = json.dumps(body, indent=4)
        # --- Запуск цикла для выполнения запросов ---
        # Если получен HTTP-код 200, то выводится содержание отчета
        # Если получен HTTP-код 201 или 202, выполняются повторные запросы
        while True:
            try:
                req = requests.post(reports_url, body, headers=headers)
                req.encoding = 'utf-8'  # Принудительная обработка ответа в кодировке UTF-8
                if req.status_code == 400:
                    print("Параметры запроса указаны неверно или достигнут лимит отчетов в очереди")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(body))
                    print("JSON-код ответа сервера: \n{}".format(req.json()))
                    result = req.json()
                    break
                elif req.status_code == 200:
                    print("Отчет создан успешно")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("Содержание отчета: \n{}".format(req.text))
                    result = req.text
                    break

                elif req.status_code == 201:
                    print("Отчет успешно поставлен в очередь в режиме офлайн")
                    retry_in = int(req.headers.get("retryIn", 60))
                    print("Повторная отправка запроса через {} секунд".format(retry_in))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    sleep(retry_in)

                elif req.status_code == 202:
                    print("Отчет формируется в режиме офлайн")
                    retry_in = int(req.headers.get("retryIn", 60))
                    print("Повторная отправка запроса через {} секунд".format(retry_in))
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    sleep(retry_in)

                elif req.status_code == 500:
                    print("При формировании отчета произошла ошибка. Пожалуйста, попробуйте повторить запрос позднее")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(req.json()))
                    result = req.json()
                    break

                elif req.status_code == 502:
                    print("Время формирования отчета превысило серверное ограничение.")
                    print("Пожалуйста, попробуйте изменить параметры запроса - уменьшить период и количество данных.")
                    print("JSON-код запроса: {}".format(body))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(req.json()))
                    result = req.json()
                    break

                else:
                    print("Произошла непредвиденная ошибка")
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(body))
                    print("JSON-код ответа сервера: \n{}".format(req.json()))
                    result = req.json()
                    break

            # Обработка ошибки, если не удалось соединиться с сервером API Директа
            except ConnectionError:
                print("Произошла ошибка соединения с сервером API")
                result = "Произошла ошибка соединения с сервером API"
                # Принудительный выход из цикла
                break

            # Если возникла какая-либо другая ошибка
            except:
                print("Произошла непредвиденная ошибка")
                result = "Произошла непредвиденная ошибка"
                # Принудительный выход из цикла
                break
        return result
