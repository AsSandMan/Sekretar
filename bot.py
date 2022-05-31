import logging
from aiogram import Bot, types
from aiogram.utils import executor
from create_bot import dp
from handlers import menu as nav


weather.register_handlers_weather(dp)
rate.register_handlers_weather(dp)
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Здравствуйте {0.first_name}".format(message.from_user), reply_markup - nav.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp)