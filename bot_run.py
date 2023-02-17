import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN
from parser import parser_uk

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

logger = logging.getLogger()

button_1 = InlineKeyboardButton(text="КРУТА пісня для тебе!!!", callback_data='button_1')
button_2 = InlineKeyboardButton(text="5 гарячих треків!!!", callback_data='button_2')
button_3 = InlineKeyboardButton(text="Година Української!!!", callback_data='button_3')

block_button = InlineKeyboardMarkup(row_width=1).add(button_1,
                                                     button_2,
                                                     button_3,
                                                     )

text = {'text_message': '<b>Виберіть потрібну кнопку</b>\n'
                        '<b>або напишіть потрібну кількість пісень</b>\n'
                        '(діє обмеження в 50 треків)',
        'raise_text': 'Щось пішло не так. Спробуйте пізніше!!!',
        'with pleasure': '<b>Слухайте із задоволенням</b>',
        'enter_a_number': 'Введіть число від 1 до 50 або натисніть кнопку'
        }


@dp.message_handler()
async def cmd_start(message: types.Message):
    if message.text.isdigit() and int(message.text) <= 50:
        number_of_song = int(message.text)
        await message.answer(text['with pleasure'])
        try:
            for k in range(number_of_song):
                await bot.send_audio(message.from_user.id,
                                     parser_uk(),
                                     )
            await bot.send_message(message.from_user.id,
                                   text['text_message'],
                                   reply_markup=block_button,
                                   )

        except TypeError:
            await bot.send_message(message.from_user.id,
                                   text['raise_text'],
                                   reply_markup=block_button,
                                   )
    else:
        await message.delete()
        await bot.send_message(message.from_user.id,
                               text['text_message'],
                               )
        await bot.send_message(message.from_user.id,
                               text['enter_a_number'],
                               reply_markup=block_button)


@dp.callback_query_handler(text='button_1')
async def button_callback(callback_query: types.CallbackQuery):
    try:
        await bot.send_message(callback_query.from_user.id,
                               text['with pleasure']
                               )
        for k in range(1):
            await bot.send_audio(callback_query.from_user.id,
                                 parser_uk(),
                                 )
        await bot.send_message(callback_query.from_user.id,
                               text['text_message'],
                               reply_markup=block_button,
                               )
    except TypeError:
        await bot.send_message(callback_query.from_user.id,
                               text['raise_text'],
                               reply_markup=block_button,
                               )


@dp.callback_query_handler(text='button_2')
async def button_callback(callback_query: types.CallbackQuery):
    try:
        await bot.send_message(callback_query.from_user.id,
                               text['with pleasure']
                               )
        for k in range(5):
            await bot.send_audio(callback_query.from_user.id,
                                 parser_uk(),
                                 )
        await bot.send_message(callback_query.from_user.id,
                               text['text_message'],
                               reply_markup=block_button,
                               )
    except TypeError:
        await bot.send_message(callback_query.from_user.id,
                               text['raise_text'],
                               reply_markup=block_button,
                               )


@dp.callback_query_handler(text='button_3')
async def button_callback(callback_query: types.CallbackQuery):
    try:
        await bot.send_message(callback_query.from_user.id,
                               text['with pleasure']
                               )
        for k in range(20):
            await bot.send_audio(callback_query.from_user.id,
                                 parser_uk(),
                                 )
        await bot.send_message(callback_query.from_user.id,
                               text['text_message'],
                               reply_markup=block_button,
                               )
    except TypeError:
        await bot.send_message(callback_query.from_user.id,
                               text['raise_text'],
                               reply_markup=block_button,
                               )
