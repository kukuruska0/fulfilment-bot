import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from bot.routes.user_router import router as core_router

load_dotenv()

bot = Bot(os.getenv('TOKEN'), parse_mode='html')
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def register_routers():
    dp.include_routers(core_router)


async def start_bot():
    register_routers()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
