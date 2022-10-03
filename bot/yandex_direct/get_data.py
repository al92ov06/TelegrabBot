from bot.yandex_direct.body_request import BodyRequest
from bot.yandex_direct.send_request import SendRequest


# Класс отвечает за получение и подготовку данных полученных от Яндекс API
class GetData:

    def get_balance(self) -> str:
        object_body_request = BodyRequest()
        object_requests_yandex = SendRequest(object_body_request.get_balance())
        data = object_requests_yandex.get_and_send_data()
        # сделать проверку наличия переменной
        result = data["data"]["Accounts"][0]["Amount"]
        return result

    def get_reports(self, data_range='TODAY', name_reports='TODAY') -> list[dict]:
        object_body_request = BodyRequest()
        object_requests_yandex = SendRequest(object_body_request.get_reports(data_range, name_reports))
        data = object_requests_yandex.get_data_table()
        # сделать проверку наличия переменной
        data = data[1:].split('\n')
        data = data[:-1]
        columns = data[1].split('\t')
        result = []
        for item in data[2:]:
            row = item.split('\t')
            di = dict(zip(columns, row))
            result.append(di)
        return result

    def get_list_campanong_on(self) -> list:
        object_body_request = BodyRequest()
        object_requests_yandex = SendRequest(object_body_request.get_id_companings_status_on())
        data = object_requests_yandex.get_and_send_data()
        # сделать проверку наличия переменной
        result = [x['Id'] for x in data['result']['Campaigns']]
        return result
