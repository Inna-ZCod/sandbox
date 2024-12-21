import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


from AT.AT03.config import TOKEN
import k_board as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

### Задание 1

# Обработка команды /start
@dp.message(CommandStart())
async def start(message: Message):
   await message.answer('Бот готов к работе!', reply_markup=kb.main)

# Обработка нажатия на Reply-кнопки
@dp.message(F.text == "Привет")
async def test_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == "Пока")
async def test_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}!')


### Задание 2

# Обработка команды /links
@dp.message(Command('links'))
async def cmd_links(message: Message):
   await message.answer('Твои любимые ссылки здесь:', reply_markup=kb.inline_keyboard_links)


### Задание 3

# Обработка команды /dynamic
@dp.message(Command('dynamic'))
async def cmd_dynamic(message: Message):
   await message.answer('Для продолжения нажми эту кнопку:', reply_markup=kb.inline_keyboard_dynamic)

# Обработка Callback
@dp.callback_query(F.data == 'sea_more')
async def show(callback: CallbackQuery):
   await callback.answer("Один момент")
   await callback.message.edit_text('Выбери нужную опцию:', reply_markup=kb.inline_keyboard_options)

@dp.callback_query(F.data == 'op_1')
async def op_1(callback: CallbackQuery):
   await callback.message.answer('Выбрана опция 1')

@dp.callback_query(F.data == 'op_2')
async def op_2(callback: CallbackQuery):
   await callback.message.answer('Выбрана опция 2')



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())