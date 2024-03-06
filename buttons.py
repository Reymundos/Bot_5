from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    btn1 = KeyboardButton('Ob-Havo')
    btn2 = KeyboardButton('Info')

    markup.add(btn1, btn2)
    return markup