from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from states.statess import txt
from keyboards.inline.togri import bb
import re



@dp.callback_query_handler(text='zakaz', state=txt.buyurtma)
async def buy(call: types.CallbackQuery):
    await call.message.answer("Buyurtmangizni shu yerga yozing")
    await call.answer(cache_time=60)
    await call.message.delete()
    await txt.text.set()

@dp.message_handler(state=txt.text)
async def get_ism(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {'data' : text}
    )
    data = await state.get_data()
    video = data.get('tanlov')
    if video == 'video' or video == 'moushn':
        await message.answer("Videoni yuboring")
        await txt.video.set()
    await txt.tanlov.set()


@dp.message_handler(content_types=['video'], state=txt.video)
async def get_img(message: types.Message, state: FSMContext):
    video = message.video.file_id           
    await state.update_data(
        {
            'video url' : video
        }
    )
    

    data = await state.get_data()
    msg = data.get("data")
   
    username =  message.from_user.username
    
    await message.answer_video(video=video, caption= f"Sizning buyurtmangiz quyidagilardan iborat:\n\nBuyurtma: \n{msg}")
    await message.answer(f"{username} Ma'lumotlar to'g'ri bo'lsa 'Ha' tugmasini bosing", reply_markup=bb)
    await txt.yuborish.set()