from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types.base import String


class CellarImport(StatesGroup):
    task = State(String)
