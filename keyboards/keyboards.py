from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def start_keybord():
    buillder = InlineKeyboardBuilder()
    buillder.add(InlineKeyboardButton(text="⚙️ Настройки", callback_data="setting"))
    return buillder.as_markup()

def settings_keybord():
    buillder = InlineKeyboardBuilder()
    buillder.add(InlineKeyboardButton(text="💭 Поменять имя", callback_data="name_change"),
                InlineKeyboardButton(text="🏠 Поменять адрес", callback_data="_change"),
                InlineKeyboardButton(text="⬅️ Вернутся", callback_data="back_to_menu"))
    
    buillder.adjust(2)
    return buillder.as_markup()