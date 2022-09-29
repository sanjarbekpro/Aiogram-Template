from loader import dp
from aiogram import types
from keyboards.inline.servis import knopka

@dp.callback_query_handler(text='back')
async def back(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://ibb.co/R6GmdL7", caption="O'zingizga kerak bo'lgan xizmat turini tanlang", reply_markup=knopka)
    await call.answer(cache_time=60)
    await call.message.delete()