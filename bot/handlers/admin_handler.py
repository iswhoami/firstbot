from aiogram import types
from aiogram.filters import Command

from app import dp, bot
from bot.filters import IsAdmin


@dp.message(Command('admin'), IsAdmin())
async def menu_admin_handler(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Я внутри admin_handler')