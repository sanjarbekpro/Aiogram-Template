from loader import dp
from aiogram import types
from keyboards.inline.kanal import kanalcha 


@dp.callback_query_handler(text='kanal')
async def xiz(call: types.CallbackQuery):
    await call.message.answer_photo(photo='https://ibb.co/R6GmdL7',caption="Sizga o'zimni kanallarimni taklif qilaman.", reply_markup=kanalcha)
    await call.answer(cache_time=60)
    await call.message.delete()