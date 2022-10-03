from telebot import types


# Меню для отправки при вызове /help и /start
def menu() -> list:
    menu = [
        '<b>Введите команду из списка (команды регистрозависимые) чтобы получить информацию:</b>',
        '',
        '   <b>Баланс</b> - /balance',
        '   <b>Статистика за день</b> - /report_day',
        '   <b>Статистика за текущий месяц</b> - /report_month',
        '   <b>Включить анализ угроз скликивания</b> - /analyze_on',
        '   <b>Остановить анализ</b> - /analyze_off',
        '   <b>Остановить все капании</b> - /stop',
        '   <b>Получить список остановленных кампаний</b> - /get_list_stop'
    ]
    return menu


def btn_menu():
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    btn_help = types.InlineKeyboardButton(text='Помощь', callback_data='Help')
    btn_balance = types.InlineKeyboardButton(text='Баланс', callback_data='Balance')
    btn_report_month = types.InlineKeyboardButton(text='Отчет за месяц', callback_data='Report month')
    btn_report_day = types.InlineKeyboardButton(text='Отчет за день', callback_data='Report day')
    btn_analyze_on = types.InlineKeyboardButton(text='Анализ', callback_data='Analyze on')
    btn_get_list_stop = types.InlineKeyboardButton(text='Компании на остановку', callback_data='Get list stop')
    btn_analyze_off = types.InlineKeyboardButton(text='Выключить анализ', callback_data='Analyze off')
    btn_stop = types.InlineKeyboardButton(text='Остановить компании', callback_data='Stop')
    keyboard_markup.add(btn_help,
                        btn_balance,
                        btn_report_month,
                        btn_report_day,
                        btn_analyze_on,
                        btn_get_list_stop,
                        btn_analyze_off,
                        btn_stop)
    return keyboard_markup
