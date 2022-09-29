from loader import dp
from aiogram import types
from keyboards.inline.byrtma import bt 
from states.statess import txt
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(text='motion', state=txt.tanlov)
async def xiz(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer_photo(photo="https://ibb.co/mHvvSqG", caption="Sizga video motion graphic xizmatini taklif qilamiz.\nHar xil turdagi reklama rolik, animation videolar tayyorlap beramiz.\n\nXizmat narxi kelishiladi.", reply_markup=bt)
    await call.answer(cache_time=60)
    await call.message.delete()
    await state.update_data(
        {'tanlov': 'moushn'}
    )
    await txt.next()