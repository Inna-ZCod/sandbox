from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ], resize_keyboard=True)

inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://ria.ru')],
    [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/home')],
    [InlineKeyboardButton(text="Видео", url='https://rutube.ru/')]
    ])


inline_keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='sea_more')]
    ])


inline_keyboard_options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data='op_1')], [InlineKeyboardButton(text="Опция 2", callback_data='op_2')]
    ])


