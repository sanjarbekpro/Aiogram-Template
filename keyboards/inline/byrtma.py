from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bt=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Buyurtma berish ✅', callback_data="zakaz")],
        [InlineKeyboardButton(text='Orqaga qaytish 🔙', callback_data='back')]

    ]
)