import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import requests

from AT.AT03.config import TOKEN, THE_CAT_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()


def get_cat_breeds():
   url = 'https://api.thecatapi.com/v1/breeds'
   headers = {"x-api-key": THE_CAT_API_KEY}
   response = requests.get(url, headers=headers)
   return response.json()


def get_cat_image_by_breed(breed_id):
   url = f'https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}'
   headers = {"x-api-key": THE_CAT_API_KEY}
   response = requests.get(url, headers=headers)
   data = response.json()
   return data[0]['url']


def get_breed_info(breed_name):
   breads = get_cat_breeds()
   for bread in breads:
      if bread['name'].lower() == breed_name.lower():
         return bread
   return None


@dp.message(CommandStart())
async def start(message: Message):
   await message.answer("Привет! Напиши породу кошки и я пришлю ее фото")


@dp.message()
async def send_cat_info(message: Message):
   breed_name = message.text
   breed_info = get_breed_info(breed_name)
   if breed_info:
      cat_image_url = get_cat_image_by_breed(breed_info['id'])
      info = (
         f"Порода - {breed_info['name']}\n"
         f"Описание - {breed_info['description']}\n"
         f"Продолжительность жизни - {breed_info['life_span']} лет"
         )
      await message.answer_photo(photo=cat_image_url, caption=info)
   else:
      await message.answer("Порода не найдена. Попробуйте еще раз.")





async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())