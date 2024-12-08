from aiogram import Bot, Dispatcher

TOKEN = "8167137587:AAHpqbeA2g8lR2l6j4_2p24WBYOm8rct1Io"
bot = Bot(TOKEN)
dp = Dispatcher()

from bot.handlers import main_handler
from bot.handlers import admin_handler
from bot.handlers import portfolio_handler
