import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import random
import requests
from datetime import datetime, timedelta

from fin_bot.config import TOKEN, NASA_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_random_apod():
    end_date = datetime.now()  # конечная дата - сегодня
    start_date = end_date - timedelta(days=365)
    random_date = start_date + (end_date - start_date) * random.random()
    date_str = random_date.strftime("%Y-%m-%d")

    url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&date={date_str}'
    response = requests.get(url)
    return response.json()

@dp.message(Command('apod'))
async def cmd_apod(message: Message):
    apod = get_random_apod()
    photo_url = apod['url']
    title = apod['title']

    await message.answer_photo(photo=photo_url, caption=f"{title}")



async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())