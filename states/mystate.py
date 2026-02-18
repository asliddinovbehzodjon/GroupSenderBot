from aiogram.filters.state import *

class NewPost(StatesGroup):
    NewMessage = State()
    