import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
import keyboard
from database import storage
from models import CellarImport

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start", 'help'])
async def cmd_test1(message: types.Message):
    await message.reply(f"Я бот для планировки твоих задач. Приятно познакомиться, {message.from_user.first_name}",
                        reply_markup=keyboard.start)


@dp.message_handler(content_types=['text'])
async def enter_task(message: types.Message):
    if message.text == "Новая задача":
        await message.answer('Как назовёте задачу?')
        await CellarImport.task.set()

@dp.message_handler(content_types=['text'])
async def enter_task(message: types.Message):
    if message.text == "Все задачи":
        await CellarImport.task.get(storage.task)


if __name__ == '__main__':
   executor.start_polling(dp)