# import requests
# from pprint import pprint
#
# city_name = 'Fergana'
#
# api_key = 'b01e7608c07f15c54ff9d9b64d478705'
#
# parameters = {
#     'q': city_name,
#     'appid': api_key,
#     'units': 'metric'
# }
#
#
# wetter = requests.get(f'https://api.openweathermap.org/data/2.5/weather?', params=parameters).json()
#
# pprint(wetter['main']['temp'])
#

from telebot import TeleBot
from telebot.types import Message

from buttons import main_menu

bot = TeleBot('7161771262:AAFJNJ1l-J0W4hJdLT2SaCQejVePiedCPrQ', parse_mode='html')

@bot.message_handler(commands=['start'])
def reaction_to_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Siz <b>Ob - Havo</b> botiga kirdingiz', reply_markup=main_menu())

@bot.message_handler(regexp='Ob-Havo')
def text(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Shahar nomini kiriting')
    bot.register_next_step_handler(msg, get_city_name)

def get_city_name(message: Message):
    chat_id = message.chat.id
    print(message.text)




if __name__ == '__main__':
    bot.infinity_polling()



