import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

import  random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://img.freepik.com/free-photo/view-beautiful-persian-domestic-cat_23-2151773826.jpg', 'https://s.zefirka.net/images/2022-06-13/milye-kotiki-zaryazhayut-pozitivom-na-snimkax/milye-kotiki-zaryazhayut-pozitivom-na-snimkax-1.jpg', 'https://s0.rbk.ru/v6_top_pics/media/img/7/65/755540270893657.jpg']
    ran_photo = random.choice(list)
    await message.answer_photo(photo=ran_photo, caption='Это супер крутая картинка')


@dp.message(F.photo)
async def ogo(message: Message):
    list = ['Ого, какая фотка!', 'Что это? Слоник?', 'Прикольно. Но скучно']
    ran_ans = random.choice(list)
    await message.answer(ran_ans)


@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer("Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ")


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())