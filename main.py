from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def quiz1(message: types.Message):
    question = 'сколько областей в Кыргызстане?'
    answers = ['6', '5', '8', '7', '10']
    button = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup = InlineKeyboardMarkup().add(button)
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        type='quiz',
                        correct_option_id=3,
                        open_period=15,
                        reply_markup=markup)


@dp.callback_query_handler(text='button_call_1')
async def quiz2(call: types.CallbackQuery):
    question = 'в каком году открылся гиктек?'
    answers = ['2017', '2018', '2019', '2020', '2021']
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        type='quiz',
                        correct_option_id=1,
                        open_period=20)


@dp.message_handler(commands=['mem'])
async def meme(message: types.Message):
    with open('media/HVQBUhCwFMY.jpg', 'rb') as photo:
        await message.answer_photo(photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
