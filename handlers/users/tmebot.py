from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.tmbot import bot 
from states.statess import txt


@dp.callback_query_handler(text='bot', state=txt.tanlov)
async def xiz(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://ibb.co/3sk21VJ", caption="Biz sizga xoxlagan turdagi botlarni yaratib beramiz.\nAgar server sotib olishga mablag'ingiz yetmasa, telegramni o'zida ham bot yaratip beramiz\n\n\nBot ochish narxi💰: 5-50$", reply_markup=bot)
    await call.answer(cache_time=60)
    await call.message.delete()
    await txt.next()