# Анализ полученных данных от Яндекс Директ на предмет скликивания
# Принимает преобразованный отчет TSV в dict
from bot.services.entry_to_file import campaign_entry_stop
from bot.yandex_direct.get_data import GetData


class AnalysesClickFraud:

    def click_fraud(self):
        return self.__analyses()

    def __get_data(self, data_range: str, name_reports: str) -> list[dict]:
        text_data = GetData().get_reports(data_range, name_reports)
        return text_data

    def __transformation_data(self, data: dict) -> list:
        list_data = []
        for clicks in data:
            list_data.append(clicks['Clicks'])
        return list_data

    # Доработать механизм (исключать периоды с аномальными данными в месячном отчете) + увеличить период анализа
    # Доработать, записывать в БД полученный от Яндекс Директ период (чтобы не тратить баллы)
    def __analyses(self) -> list:
        reports_month = self.__get_data(data_range='THIS_MONTH', name_reports='THIS_MONTH')
        reports_today = self.__get_data(data_range='TODAY', name_reports='TODAY')
        campaign_stop_list = []

        for data_today in reports_today:
            clicks_today = int(data_today['Clicks'])
            companing_id_today = data_today['CampaignId']
            list_clicks_max = []

            for data_month in reports_month:

                if companing_id_today == data_month['CampaignId']:
                    list_clicks_max.append(int(data_month['Clicks']))
            list_clicks_max = max(list_clicks_max)

            if clicks_today < list_clicks_max:
                campaign_stop_list.append(companing_id_today)

        campaign_entry_stop(campaign_stop_list)
        return campaign_stop_list
