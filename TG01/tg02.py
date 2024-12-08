import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from gtts import gTTS
import os
from googletrans import Translator
import subprocess
import logging

from config import TOKEN

##########################################
#
# ВНИМАНИЕ !!!
#
# Если вы копируете себе этот код, убедитесь, что на вашем устройстве установлен FFmpeg
# Только в этом случае код будет работать в полном функционале
#
# Если FFmpeg не установлен, вам будет доступен только текстовый режим работы
# Голосовой режим работать не будет, для него нужен FFmpeg
#
###########################################

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
translator = Translator()

s_text = True  # Флаг для переключения режимов Голос/текст

# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
    logging.info(f"Пользователь {message.from_user.id} начал диалог.")
    await message.answer(f"Привет, {message.from_user.first_name}")


# Обработчик команды /help
@dp.message(Command('help'))
async def cmd_help(message: Message):
    help_text = (
        "📄 **Возможности бота**:\n"
        "- Пришли мне изображение — я его сохраню.\n"
        "- Напиши текст — я переведу его на английский.\n"
        "- Команда /voice — отвечаю голосом.\n"
        "- Команда /text — отвечаю текстом.\n"
    )
    await message.answer(help_text, parse_mode="Markdown")

# Обработчик фото пользователя
@dp.message(F.photo)
async def ogo(message: Message):
    await message.answer("Изображение сохранено")
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

# Переключение на текстовый режим
@dp.message(Command('text'))
async def cmd_text(message: Message, state: FSMContext):
    await state.update_data(mode="text")
    await message.answer("Текстовый режим включён.")

# Переключение на голосовой режим
@dp.message(Command('voice'))
async def cmd_voice(message: Message, state: FSMContext):
    await state.update_data(mode="voice")
    await message.answer("Голосовой режим включён.")

# Переводчик
@dp.message()
async def trans(message: Message, state: FSMContext):
    user_data = await state.get_data()
    mode = user_data.get("mode", "text")
    translated = translator.translate(message.text, dest='en')
    if mode == "text":
        await message.answer(translated.text)
    else:
        try:
            # Проверяем, установлен ли FFmpeg
            subprocess.run(['ffmpeg', '-version'], check=True)
        except FileNotFoundError:
            logging.error("FFmpeg не установлен. Пожалуйста, установите FFmpeg.")
            await message.answer("Ошибка: FFmpeg не найден. Установите его и повторите попытку.")
            return

        try:
            # Генерация MP3-файла
            tts = gTTS(text=translated.text, lang='en')
            tts.save('trans.mp3')

            # Конвертация MP3 в OGG с использованием FFmpeg
            ogg_filename = 'trans.ogg'
            subprocess.run(
                ['ffmpeg', '-y', '-i', 'trans.mp3', '-acodec', 'libopus', ogg_filename],
                check=True)

            # Отправка OGG как голосового сообщения
            audio_file = FSInputFile(ogg_filename)
            await bot.send_voice(message.chat.id, audio_file)

            # Удаление временных файлов
            os.remove('trans.mp3')
            os.remove(ogg_filename)
        except subprocess.CalledProcessError as e:
            await message.answer("Ошибка при конвертации в OGG. Проверьте установку FFmpeg.")
        except Exception as e:
            await message.answer(f"Произошла ошибка: {e}")


# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())