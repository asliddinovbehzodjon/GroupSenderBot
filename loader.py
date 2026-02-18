from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from data import config
from aiogram.enums import ParseMode
from utils.dp_api.sqlite import *
bot = Bot(config.BOT_TOKEN,parse_mode='HTML'
    )
stroge = MemoryStorage()
dp = Dispatcher(storage=stroge)
db = Database(path_to_db="data/main.db")