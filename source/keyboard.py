from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import db


def select_direction_kb():
    keyboard_list = []
    for row in db.database('select_direction', None, None):
        keyboard_list.append(
            [InlineKeyboardButton(row, callback_data='select_direction'+'|'+row)])
    return InlineKeyboardMarkup(inline_keyboard=keyboard_list)