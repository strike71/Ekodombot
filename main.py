
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from conversation import register_handlers

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
