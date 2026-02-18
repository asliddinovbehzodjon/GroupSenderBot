# Admin Button
from aiogram.utils.keyboard import ReplyKeyboardBuilder,KeyboardButton
def admin_button():
    button = ReplyKeyboardBuilder()
    button.row(

        KeyboardButton(text="📊 Guruhlar soni"),
        KeyboardButton(text="🗣 Reklama yuborish")

    )
   

    button.adjust(2,2)
    return button.as_markup(resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Kerakli bo'limni tanlang!")
