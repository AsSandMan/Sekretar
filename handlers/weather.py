from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from config import open_weather_token
import requests
import datetime






class FSMadmin(StatesGroup):
    city = State()
    weather_info = State()

# Запускаем функцию погоды
# @dp.message_handler(commands="погода", state = None)
async def city(message: types.Message):
    await message.reply('Напишите город в котором хотите узнать погоду')
    await FSMadmin.city.set()
    # print('Начало программы')

# Ловим название города
# @dp.message_handler(content_types=['text'], state = FSMadmin.city)
async def city_set(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = str(message.text)
    await FSMadmin.next()
    # print('Принятие программы')


# Получаем данные погоды из города  
# @dp.message_handler(state=FSMadmin.weather_info)
# async def weather(message: types.Message, state: FSMContext):
    # print('Обработка погоды')
    async with state.proxy() as data:
        Change_city = str(data['city'])
    
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={Change_city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.answer(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"***Хорошего дня!***"
              )

    except:
        await message.answer("\U00002620 Проверьте название города \U00002620")
    
    await state.finish()

    
# регистрируем хендлеры
def register_handlers_weather(dp : Dispatcher):
    dp.register_message_handler(city, commands=["погода"],state=None)
    dp.register_message_handler(city_set, state=FSMadmin.city)
    

   