from loader import dp
from aiogram import types
from keyboards.inline.asos import menu
from states.statess import txt

@dp.callback_query_handler(text='orqa', state=txt.buyurtma)
async def back(call: types.CallbackQuery):
    await call.message.answer_photo(photo='https://ibb.co/R6GmdL7', caption='Bosh menudasiz\nBiz sizga o\'z IT xizmatlarimizni taklif qilamiz\n\nQuyidagilardan birini tanlang👇', reply_markup=menu)
    await call.answer(cache_time=60)
    await call.message.delete()
    await txt.tanlov.set()