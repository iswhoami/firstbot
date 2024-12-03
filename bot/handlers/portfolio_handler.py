from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

from app import dp, bot
from bot.filters import IsAdmin


class PortfolioForm(StatesGroup):
    desc = State()
    photo = State()
    audio = State()


@dp.callback_query(F.data == 'add_portfolio_item', IsAdmin())
async def add_portfolio_item(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await bot.send_message(call.message.chat.id, text='Пришли краткое описание для добавляемой работы')
    await state.set_state(PortfolioForm.desc)


@dp.message(F.text, PortfolioForm.desc)
async def add_portfolio_item(message: Message, state: FSMContext):
    desc = message.text
    await state.update_data(desc=desc)
    await bot.send_message(message.chat.id, text='Пришли фото обложки для добавляемой работы')
    await state.set_state(PortfolioForm.photo)


@dp.message(F.photo, PortfolioForm.photo)
async def add_portfolio_item(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)
    await bot.send_message(message.chat.id, text='Пришли аудио для добавляемой работы')
    await state.set_state(PortfolioForm.audio)


# если фото отправляется в виде файла
@dp.message(F.document.mime_type.startswith('image/'), PortfolioForm.photo)
async def add_portfolio_item(message: Message, state: FSMContext):
    photo_id = message.document.file_id
    await state.update_data(photo=photo_id)
    await bot.send_message(message.chat.id, text='Пришли аудио для добавляемой работы')
    await state.set_state(PortfolioForm.audio)


@dp.message(F.document, PortfolioForm.audio)
async def add_portfolio_item(message: Message, state: FSMContext):
    photo_id = message.document.file_id
    await state.update_data(photo=photo_id)
    await bot.send_message(message.chat.id, text='Пришли аудио для добавляемой работы')
    await state.set_state(PortfolioForm.audio)