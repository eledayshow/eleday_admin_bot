import asyncio
import logging
from aiogram import Bot, Dispatcher
import conf

from handlers import text_messages


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=conf.bot_token)
    dp = Dispatcher()

    dp.include_routers(
        text_messages.router
    )

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
