from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kanalcha=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Sanajrbek - IT blog', url="https://t.me/RajapovSanjarbek")],
        [InlineKeyboardButton(text='Sanjarbek Rajapov', url="https://t.me/Sanjarbek_Rajapov")],
        [InlineKeyboardButton(text="Qur'on tv", url="https://t.me/qisqa_suralar")],
        [InlineKeyboardButton(text="Orqaga qaytish 🔙", callback_data='orqa')]
   ]
)