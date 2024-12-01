from aiogram import types


def main_keyboard():
    """ Главная клавиатура """

    kb = [
        [types.KeyboardButton(text="Обо мне")],
        [types.KeyboardButton(text="Портфолио")],
        [types.KeyboardButton(text="Написать мне")],
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

