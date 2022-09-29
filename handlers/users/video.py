from loader import dp
from aiogram import types
from keyboards.inline.byrtma import bt 
from aiogram.dispatcher.storage import FSMContext
from states.statess import txt


@dp.callback_query_handler(text='vid', state=txt.tanlov)
async def xiz(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer_photo(photo="https://ibb.co/c2xfzFk", caption="Sizga video mantaj xizmatini taklif qilamiz.\nHar xil turdagi videolarni mantaj qilip beramiz.\n\nXizmat narxi kelishiladi.", reply_markup=bt)
    await call.answer(cache_time=60)
    await call.message.delete()
    await state.update_data(
        {'tanlov': 'video'}
    )
    await txt.buyurtma.set()