import sqlite3
from loader import dp, bot
from aiogram import types
from data.config import ADMINS
from states.statess import txt
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(text='yes', state=txt.yuborish)
async def zn(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    video = data.get('tanlov')
    video_url = data.get('video url')
    if video == 'video':
        msg = data.get('data')
        user = call.from_user.username
        first = call.from_user.first_name
        if user == None:
            await bot.send_video(1632373440, video_url, caption=f"{first}\n{msg}")
        else:
            await bot.send_video(1632373440, video_url, caption=f"{user}\n{msg}")
        await call.message.answer(f"Ma'lumotlaringiz qabul qilindi!")
        await call.answer(cache_time=60)
        await state.finish()
    else:
        data = await state.get_data()
        msg = data.get('data')
        user = call.from_user.username
        first = call.from_user.first_name
        if user == None:
            await bot.send_message(1632373440, text=f"{first}\n{msg}")
        else:
            await bot.send_message(1632373440, text=f"{user}\n{msg}")
        await call.message.answer(f"Ma'lumotlaringiz qabul qilindi!")
        await call.answer(cache_time=60)
        await state.finish()
    # await call.message.delete()