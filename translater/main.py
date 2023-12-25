from deep_translator import GoogleTranslator
from aiogram import Dispatcher, Bot, executor, types
from texts import *


API_TOKEN = "BOT_TOKEN"

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

arr_languages = [lang for lang in languages.strip('\n').split('\n')]
language_codes = ['ru', 'en', 'es', 'it', 'fr', 'de', 'ja', 'uk', 'tr', 'ar']


lang_kb = types.InlineKeyboardMarkup()
for i in range(len(arr_languages)):
    lang_kb.add(types.InlineKeyboardButton(arr_languages[i], callback_data=language_codes[i]))

def translate_text(text, lang_code):
    return GoogleTranslator('auto', lang_code).translate(text)

@dp.message_handler(commands=['start'])
async def say_hello(msg: types.Message):
    await msg.answer(hello)

@dp.callback_query_handler()
async def catch_btns(cback: types.CallbackQuery):
    cback_data = cback.data
    await cback.message.edit_text(translate_text(cback.message.text, cback_data), reply_markup=lang_kb)

@dp.message_handler()
async def send_text(msg: types.Message):
    await msg.answer(msg.text, reply_markup=lang_kb)

if __name__ == '__main__':
    executor.start_polling(dp)