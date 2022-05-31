from aiogram import types, Dispatcher
from create_bot import dp
from config import Fixer_token
import requests
import datetime



async def currency(message: types.Message):
    r = requests.get(
                f"http://data.fixer.io/api/latest?access_key={Fixer_token}"
            )
    data = r.json()

    USD = data["rates"]["USD"]
    RUB = data["rates"]["RUB"]

    EUR_R = RUB
    USD_R = RUB / USD

    await message.answer(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
    """Текущий курс валют\n"""
    f"""Доллар : {USD_R:.{2}f}\n"""
    f"""Евро: {EUR_R:.{2}f}"""
    )

def register_handlers_weather(dp : Dispatcher):
    dp.register_message_handler(currency, commands=["Курс"])