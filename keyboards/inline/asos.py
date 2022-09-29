from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='IT xizmatlar ♻️', callback_data='xizmat'), InlineKeyboardButton(text='Kanallarim 📡', callback_data='kanal')]
    ]
)