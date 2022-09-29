from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

knopka=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Telegram bot yaratish 🤖', callback_data='bot')],
        [InlineKeyboardButton(text='Sayt yaratish 📈', callback_data='sayt')],
        [InlineKeyboardButton(text='Video mantaj 🎥', callback_data='vid')],
        [InlineKeyboardButton(text='Motion graphic 🎞', callback_data='motion')],
        [InlineKeyboardButton(text='Grafik dizayn 🗾', callback_data='grafik')],
        [InlineKeyboardButton(text='Orqaga qaytish 🔙', callback_data='orqa')]

    ]
)