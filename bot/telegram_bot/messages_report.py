# Разметка и формирование сообщения ежедневный отчет
def messages_report(data: list[dict]):
    strings = []
    for text in data:
        date = text['Date']
        id_c = text['CampaignId']
        name = text['CampaignName']
        impressions = text['Impressions']
        clicks = text['Clicks']
        ctr = text['Ctr']
        cost = text['Cost']
        str_s = f'<b>---{date}</b> \n{id_c}  {name}\n' \
                f'Impressions - <b>{impressions}</b> | ' \
                f'Clicks - <b>{clicks}</b> | ' \
                f'CTR - <b>{ctr}</b> | ' \
                f'Cost - <b>{cost} руб.</b>\n' \
                f'- - - - - - - - - - - -'
        strings.append(str_s)
    return strings
