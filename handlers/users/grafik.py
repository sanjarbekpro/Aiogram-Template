from loader import dp
from aiogram import types
from keyboards.inline.tmbot import bot 


@dp.callback_query_handler(text='grafik')
async def xiz(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://ibb.co/NrdN2Qs", caption="Sizga grafik dizayn xizmatini taklif qilamiz.\nHar xil turdagi reklama postlar, banner, vizitka, instagramga post dizaynlarini tayyorlap beramiz.\n\nXizmat narxi 💰: 30 000 dan 70 000 gacha.", reply_markup=bot)
    await call.answer(cache_time=60)
    await call.message.delete()