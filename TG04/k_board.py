from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

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



# test = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]
#
# async def test_keyboard():
#    keyboard = InlineKeyboardBuilder()
#    for key in test:
#        keyboard.add(InlineKeyboardButton(text=key, url='<https://www.youtube.com/watch?v=HfaIcB4Ogxk>'))
#    return keyboard.adjust(2).as_markup()