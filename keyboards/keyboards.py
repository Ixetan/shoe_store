from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def start_keybord():
    buillder = InlineKeyboardBuilder()
    buillder.add(InlineKeyboardButton(text="⚙️ Настройки", callback_data="setting"))
    return buillder.as_markup()

def settings_keybord():
    buillder = InlineKeyboardBuilder()
    buillder.add(InlineKeyboardButton(text="💭 Поменять имя", callback_data="name_change"),
                InlineKeyboardButton(text="🏠 Поменять адрес", callback_data="addresser_settings"),
                InlineKeyboardButton(text="⬅️ Вернутся", callback_data="back_to_menu"))
    
def addresses_keybord():
    buillder = InlineKeyboardBuilder

    buillder.add(
        InlineKeyboardButton(text="➕ ", callback_data="add_addess"),
        InlineKeyboardButton(text="⬅️ Вернутся", callback_data="back_to_menu")
    )

    buillder.adjust(2, 1, 1)
    return buillder.as_markup()