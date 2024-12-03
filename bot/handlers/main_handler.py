import aiofiles

from aiogram import types
from aiogram.filters import Command
from aiogram import F
from aiogram.types import FSInputFile

from app import bot, dp
from bot.keyboards import main_keyboard
from config import PHOTO_PATH, INTERVIEW_PATH, PORTFOLIO_PATH, MY_LINK_PATH


@dp.message(Command('start'))
async def start_handler(message: types.Message):
    photo = FSInputFile(PHOTO_PATH)
    async with aiofiles.open(INTERVIEW_PATH, 'r', encoding='utf-8') as text_file:
        text = await text_file.read()
    keyboard = main_keyboard()
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         caption=text,
                         reply_markup=keyboard)


@dp.message(F.text == "Обо мне")
async def menu_about_handler(message: types.Message):
    photo = FSInputFile(PHOTO_PATH)
    async with aiofiles.open(INTERVIEW_PATH, 'r', encoding='utf-8') as text_file:
        text = await text_file.read()
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=text)


@dp.message(F.text == "Портфолио")
async def menu_portfolio_handler(message: types.Message):
    async with aiofiles.open(PORTFOLIO_PATH, 'r', encoding='utf-8') as text_file:
        link = await text_file.read()
    link = link.rstrip()
    kb = [
        [types.InlineKeyboardButton(text="Открыть", url=link)],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await bot.send_message(chat_id=message.chat.id,
                           text='Моё портфолио доступно на github. Ты можешь с ним ознакомиться, нажав на кнопку.',
                           reply_markup=keyboard)


@dp.message(F.text == "Связаться со мной")
async def menu_message_me_handler(message: types.Message):
    async with aiofiles.open(MY_LINK_PATH, 'r', encoding='utf-8') as text_file:
        link = await text_file.read()
    kb = [
        [types.InlineKeyboardButton(text="Написать", url=link)],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await bot.send_message(chat_id=message.chat.id,
                           text='Напиши мне в личные сообщения, я открыт миру :)',
                           reply_markup=keyboard)
