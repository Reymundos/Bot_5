from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    btn1 = KeyboardButton('Ob-Havo')
    btn2 = KeyboardButton('Info')

    markup.add(btn1, btn2)
    return markup

def city_button():
    markup_c = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    c_btn1 = KeyboardButton('City')
    c_btn2 = KeyboardButton('Location')

    markup_c.add(c_btn1, c_btn2)
    return markup_c