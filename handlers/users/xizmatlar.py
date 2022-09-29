from loader import dp
from aiogram import types
from keyboards.inline.servis import knopka 
from aiogram.dispatcher.storage import FSMContext
from states.statess import txt 


@dp.callback_query_handler(text='xizmat')
async def xiz(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer_photo(photo="https://ibb.co/R6GmdL7", caption="O'zingizga kerak bo'lgan xizmat turini tanlang", reply_markup=knopka)
    await call.answer(cache_time=60)
    await call.message.delete()
    await txt.tanlov.set()
    