import logging
import asyncio
import sys

from aiogram import Bot, Dispatcher
from config import Settings
from handlers import start, capture

settings = Settings(_env_file='.env')
bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher()


async def main():
	# await restart_bot()
	# print('Starting bot...')
	logging.info("********** BOT IS STARTED! **********")
	# dp.update.middleware(LoggingMiddleware())
	dp.include_router(start.router)
	dp.include_router(capture.router)

	await dp.start_polling(bot)


if __name__ == '__main__':
	logging.basicConfig(
		level=logging.INFO,
		stream=sys.stdout,
		# filename='data/bot_updates.log',
		format=
		'[{asctime}] #{levelname:8} {filename}:'
		'{lineno} - {name} - {message}',
		style='{'
	)
	try:
		asyncio.run(main())
	except (KeyboardInterrupt, SystemExit):
		logging.error("Bot stopped!")
