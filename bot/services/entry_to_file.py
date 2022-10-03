# Запись компаний с подозрением на скликивание в файл
def campaign_entry_stop(data: list):
    with open('bot/logs/list_stop_campaign.txt', 'w') as file:
        for item in data:
            file.write(item + '\n')
