import aiohttp
import asyncio
from loader import db
import requests
import json
from environs import Env
env = Env()
env.read_env()
# URL = env.str('URL')

async def create_user(chat_id:str,name:str=None):
    print(chat_id,name)
    info = db.select_user(chat_id=chat_id)
    print(info)
    try:
        if info == {} or info is None:
           db.add_user(chat_id=chat_id,name=name)
        else:
            pass
    except Exception as e:
        print(e)
        pass
async def get_all_users():
    try:
        data = db.select_all_users()
        return data
    except:
        return []
async def get_user(chat_id):
    try:
        data = db.select_user(chat_id=chat_id)
        return data
    except:
        return {}
async def users_count():
    try:
        data = db.count_users()
        return data[0]
    except:
        return 0
