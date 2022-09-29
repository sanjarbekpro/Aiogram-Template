from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Buyurtma berish ✅', callback_data="buyurtma")],
        [InlineKeyboardButton(text='Orqaga qaytish 🔙', callback_data='back')]

    ]
)