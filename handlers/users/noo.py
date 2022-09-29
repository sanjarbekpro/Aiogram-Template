import sqlite3
from loader import dp
from aiogram import types
from keyboards.inline.servis import knopka





@dp.callback_query_handler(text='no')
async def zn(call: types.CallbackQuery):
    await call.message.answer(f"Ma'lumotlaringiz bekor qilindi")
    await call.message.answer_photo(photo="https://ibb.co/R6GmdL7", caption="O'zingizga kerak bo'lgan xizmat turini tanlang", reply_markup=knopka)
    await call.answer(cache_time=60)
    await call.message.delete()