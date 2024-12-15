import asyncio
import aiohttp
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from googletrans import Translator
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

# Функция для получения данных с сайта numbersapi.com в формате JSON
async def fetch_number_fact(number: str, fact_type: str) -> dict:
    url = f"http://numbersapi.com/{number}/{fact_type}?json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            return None

# Функция для перевода текста с английского на русский с помощью googletrans
async def translate_to_russian(text: str) -> str:
    return translator.translate(text, src="en", dest="ru").text if text else None

# Функция для преобразования числа в формат даты (месяц/день)
def convert_to_date(number: int):
    potential_dates = []

    if 10 <= number <= 99:  # Двузначные числа
        month = number // 10
        day = number % 10
        if 1 <= month <= 12 and 1 <= day <= 31:
            potential_dates.append(f"{month}/{day}")

    elif 100 <= number <= 999:  # Трехзначные числа
        month1 = number // 100
        day1 = number % 100
        if 1 <= month1 <= 12 and 1 <= day1 <= 31:
            potential_dates.append(f"{month1}/{day1}")

        month2 = number // 10
        day2 = number % 10
        if 1 <= month2 <= 12 and 1 <= day2 <= 31:
            potential_dates.append(f"{month2}/{day2}")

    elif 1000 <= number <= 1231:  # Четырехзначные числа
        month = number // 100
        day = number % 100
        if 1 <= month <= 12 and 1 <= day <= 31:
            potential_dates.append(f"{month}/{day}")

    return potential_dates

# Обработчик команды /start
@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет! Напиши любое число, и я расскажу о нем что-нибудь интересное.")

# Обработчик для получения информации о числе
@dp.message()
async def number_fact_handler(message: Message):
    number = message.text.strip()

    if not number.isdigit():
        await message.answer("Пожалуйста, введите корректное число.")
        return

    fact_types = ["trivia", "math", "date", "year"]
    facts = []

    for fact_type in fact_types:
        if fact_type == "date":
            date_variants = convert_to_date(int(number))
            if not date_variants:
                continue
            date_variant = random.choice(date_variants)
            fact_data = await fetch_number_fact(date_variant, fact_type)
        else:
            fact_data = await fetch_number_fact(number, fact_type)

        if fact_data and fact_data.get("found"):
            translated_fact = await translate_to_russian(fact_data.get("text"))
            facts.append((fact_type, translated_fact))

    if not facts:
        response = f"Число {number} оказалось очень скучным. Попробуйте другое число!"
    else:
        response_parts = [f"Вот что я нашел про число {number}:"]
        for fact_type, translated_fact in facts:
            type_translation = {
                "trivia": "Общие факты",
                "math": "Математические факты",
                "date": "Факты о датах",
                "year": "Факты о годах"
            }.get(fact_type, fact_type)
            response_parts.append(f"• {type_translation}: {translated_fact}")
        response = "\n\n".join(response_parts)

    await message.answer(response)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



