from body_request import BodyRequest
from send_request import SendRequest


class SendData:
    def stop_all_company(self):
        # Получаем список Id запущенных кампаний
        object_body_request = BodyRequest()
        object_requests_yandex = SendRequest(object_body_request.get_id_companings_status_on())
        data = object_requests_yandex.get_and_send_data()
        data = data['result'].get('Campaigns', False)
        if data:
            info = data
            id_list = [x['Id'] for x in info]
            # Останавливаем запущенные РК

            result = self.__stop_company(id_list)
            # Сохраняем список остановленных РК
            with open('../logs/yandex_direct/stop_campaigns.txt', 'w') as file:
                for li in id_list:
                    file.write(str(li) + '\n')
        else:
            result = 'Список активных кампаний пуст, проверь те через интерфейс!'

        return result

    # Останавливаем запущенные РК
    def __stop_company(self, id_list: list) -> list:
        object_body_request = BodyRequest()
        ya_api_suspend = SendRequest(object_body_request.suspend(id_list))
        result = ya_api_suspend.get_and_send_data()
        return result

    def __start_campany(self):
        pass
