from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton('⬅ Главное меню')

#'''Main menu'''
buttonWeather = KeyboardButton('Узнать погоду 🌂 ')
buttonRate = KeyboardButton('Узнать курс валют 💲 ')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonWeather, buttonRate)

#'''WeatherMenu'''
buttonYour_City = KeyboardButton(f'Узнать погоду в Вашем городе 🌂 ')
buttonChange_City = KeyboardButton('Узнать погоду в другом городе ☀ ')
weatherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonYour_City, buttonChange_City)


