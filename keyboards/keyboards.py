from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def start_keybord():
    buillder = InlineKeyboardBuilder()
    buillder.add(InlineKeyboardBuilder(text="Настройки", callback_date="setting"))
    buillder.adjust(3)
    return buillder.as_markup()