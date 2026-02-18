from aiogram.filters import CommandStart,Command
from aiogram import types,F,html
from loader import dp,bot
from filters import IsPrivate,IsChatAdmin
from keyboards.default.buttons import *
from aiogram.fsm.context import FSMContext
from api import *
from states.mystate import NewPost
def test_button_back():
    button = ReplyKeyboardBuilder()
   
    button.row(
        
        KeyboardButton(text="⬅️ Orqaga")
        
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
@dp.message(CommandStart(),IsPrivate(),IsChatAdmin())
async def start(message:types.Message):
    text = (f"Assalomu alaykum!\n"
            f"Boss,Meni guruhlarga qo'shing va rekalamalarni yuboring!\n"
            )
    from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
    button = InlineKeyboardBuilder()
    bot_me = await bot.get_me()
    button.button(text="Guruhga qo'shish",url=f'https://t.me/{bot_me.username}?startgroup=true')

    await message.answer(text=text,reply_markup=button.as_markup())
    await message.answer('🔝 Asosiy sahifa',reply_markup=admin_button())
@dp.message(F.text=="📊 Guruhlar soni",IsPrivate(),IsChatAdmin())
async def start(message:types.Message):
    counting = await users_count()
    tekst = f"Bot hozirda {counting} ta guruhga a'zo!"
    await message.answer(html.bold(tekst),reply_markup=admin_button())
@dp.message(F.text=="🗣 Reklama yuborish",IsChatAdmin())
async def start(message:types.Message,state:FSMContext):
    await message.answer(html.bold('Reklama matnini yuboring!'),reply_markup=test_button_back())
    await state.set_state(NewPost.NewMessage)
@dp.message(NewPost.NewMessage,IsPrivate(),IsChatAdmin())
async def start(message:types.Message,state:FSMContext):
    if message.text=="⬅️ Orqaga":
         await message.answer('🔝 Asosiy sahifa',reply_markup=admin_button())
         await state.clear()
    else:
        counter = 0
        users = await get_all_users()
        try:
            
            for user in users:
                await bot.copy_message(
                chat_id=user[1],
                from_chat_id=message.chat.id,
                message_id=message.message_id,
                
            )
                await asyncio.sleep(1)
                counter+=1
        except:
            pass
        await message.answer(html.bold(f"{counter} ta guruhga xabar yuborildi!"))
        await state.clear()

