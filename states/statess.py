# from email.mime import image
from aiogram.dispatcher.filters.state import State, StatesGroup

class txt(StatesGroup):
    tanlov = State()
    buyurtma = State()
    text = State()
    yuborish = State()
    video = State()
    toxta = State()
    