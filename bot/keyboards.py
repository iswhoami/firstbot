from aiogram import types


def main_keyboard():
    """ Главная клавиатура """

    kb = [
        [types.KeyboardButton(text="Обо мне")],
        [types.KeyboardButton(text="Портфолио")],
        [types.KeyboardButton(text="Связаться со мной")]
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def admin_keyboard():
    kb = [
        [types.InlineKeyboardButton(text="Добавить работу в портфолио", callback_data='add_portfolio_item')],
        [types.InlineKeyboardButton(text="Убрать работу из портфолио", callback_data='remove_portfolio_item')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard
