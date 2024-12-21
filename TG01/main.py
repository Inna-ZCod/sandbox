import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from gtts import gTTS
import os

from AT.AT03.config import TOKEN
import keyboard as kb

import  random


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.test_keyboard())


# Обработчик команды /video
@dp.message(Command('video'))
async def cmd_video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('TG01.mp4')
    await bot.send_video(message.chat.id, video)


# Обработчик команды /doc
@dp.message(Command('doc'))
async def cmd_doc(message: Message):
    doc = FSInputFile('file.pdf')
    await bot.send_document(message.chat.id, doc)


# Обработчик команды /voice
@dp.message(Command('voice'))
async def cmd_voice(message: Message):
    voice = FSInputFile('file.ogg')
    await bot.send_voice(message.chat.id, voice)
    # await message.answer_voice(voice)


# Обработчик команды /audio
@dp.message(Command('audio'))
async def cmd_audio(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_audio')
    audio = FSInputFile('')
    await bot.send_audio(message.chat.id, audio)


# Обработчик команды /train
@dp.message(Command('train'))
async def cmd_train(message: Message):
    training_list = [
        "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_tr = random.choice(training_list)
    await message.answer(f'Это тренировка на сегодня: \n{rand_tr}')

    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('train.mp3')
    audio = FSInputFile('train.mp3')
    await bot.send_audio(message.chat.id, audio)
    os.remove('train.mp3')


# Обработчик команды фото
@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://img.freepik.com/free-photo/view-beautiful-persian-domestic-cat_23-2151773826.jpg', 'https://s.zefirka.net/images/2022-06-13/milye-kotiki-zaryazhayut-pozitivom-na-snimkax/milye-kotiki-zaryazhayut-pozitivom-na-snimkax-1.jpg', 'https://s0.rbk.ru/v6_top_pics/media/img/7/65/755540270893657.jpg']
    ran_photo = random.choice(list)
    await message.answer_photo(photo=ran_photo, caption='Это супер крутая картинка')

# Обработчик фото пользователя
@dp.message(F.photo)
async def ogo(message: Message):
    list = ['Ого, какая фотка!', 'Что это? Слоник?', 'Прикольно. Но скучно']
    ran_ans = random.choice(list)
    await message.answer(ran_ans)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')

# Обработчик ключевой фразы
@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer("Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ")

# Обработчик команды /help
@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=kb.inline_keyboard_test)

# Обработчик неопознанного сообщения от пользователя (эхо бот)
@dp.message()
async def text(message: Message):
    await message.send_copy(chat_id=message.chat.id)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())