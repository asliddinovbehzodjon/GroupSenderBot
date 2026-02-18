import asyncio
import datetime
from aiogram.filters import CommandStart,Command
from currency import get_currency
from aiogram import types
from loader import dp,bot
from filters import IsPrivate,IsGroup,CheckMessage
from aiogram.filters import ChatMemberUpdatedFilter,IS_NOT_MEMBER,ADMINISTRATOR
from aiogram.types import ChatMemberUpdated
from aiogram.enums import ChatMemberStatus
from aiogram import html
from data.config import ADMINS
from api import *
text = "Assalomu alaykum!\nGuruppa hamma ishla joyidami?"
@dp.my_chat_member(IsGroup())
async def bot_added_to_group(event: ChatMemberUpdated):
    old_status = event.old_chat_member.status
    new_status = event.new_chat_member.status

    # Bot was added to a group
    if old_status in {ChatMemberStatus.LEFT, ChatMemberStatus.KICKED} \
       and new_status in {ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR}:

        added_by = event.from_user
        chat = event.chat
        await create_user(chat_id=chat.id,name=chat.title)  
        print(ADMINS) 
        tekst = f"✅ Bot yangi guruhga qo'shildi!\n\n"\
                f"✅ Bot nomi:{chat.title}\n"\
                f"✅ Bot username: {chat.username}\n"    
                 
        for i in ADMINS:
            await bot.send_message(
                chat_id=i,
                text=html.bold(tekst)
            )