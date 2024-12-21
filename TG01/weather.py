import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

from AT.AT03.config import TOKEN, OPENWEATHER_API_KEY, CITY_NAME


# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

# функция для получения погоды из OpenWeather API
def get_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={OPENWEATHER_API_KEY}&lang=ru&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"Погода в {CITY_NAME}:\nТемпература: {temp}°C\nОписание: {description}"
    else:
        return "Не удалось получить прогноз погоды. Попробуйте позже."

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот погоды для города Благовещенск.\n" 
                         "Используйте /weather чтобы узнать погоду.")

# Обработчик команды /help
@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Я умею сообщать погоду в городе Благовещенск. Используй команду /weather для получения прогноза.")


# Обработчик команды /weather
@dp.message(Command("weather"))
async def cmd_weather(message: Message):
    weather_info = get_weather()
    await message.answer(weather_info)

# Обработчик всех остальных сообщений
@dp.message(F.text)
async def cmd_default(message: Message):
    await message.answer("Я умею только предсказывать погоду в городе Благовещенск.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

