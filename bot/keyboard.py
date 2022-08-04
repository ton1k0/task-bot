from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


start = types.ReplyKeyboardMarkup(resize_keyboard=True)

all_tasks = types.KeyboardButton("Все задачи")
new_task = types.KeyboardButton("Новая задача")

start.add(all_tasks, new_task)