from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.tmbot import bot 
from states.statess import txt


@dp.callback_query_handler(text='sayt', state=txt.tanlov)
async def xiz(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer_photo(photo="https://ibb.co/Fb98S2q", caption="Biz sizga sayt yaratish xizmatini taklif qilamiz\nSizga qanaqa sayt kerak?\n\n\nSayt ochish narxi💰: Sayt turiga qarab belgilanadi.", reply_markup=bot)
    await call.answer(cache_time=60)
    await call.message.delete()
    await txt.next()