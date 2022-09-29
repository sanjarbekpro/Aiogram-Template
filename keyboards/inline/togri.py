from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='HA', callback_data="yes"), InlineKeyboardButton(text="YO'Q", callback_data='no')]
        

    ]
)