from aiogram import types
from aiogram.filters import Command

from app import dp, bot
from bot.filters import IsAdmin
from bot.keyboards import admin_keyboard


@dp.message(Command('admin'), IsAdmin())
async def menu_admin_handler(message: types.Message):
    keyboard = admin_keyboard()
    await bot.send_message(chat_id=message.chat.id, text='Выберите действие', reply_markup=keyboard)


