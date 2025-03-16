from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from wares.wares import wares



def start_keybord():
    buillder = InlineKeyboardBuilder()
    buillder.add(InlineKeyboardButton(text="🛍️ Каталог", callback_data="catalogue"),
                 InlineKeyboardButton(text="⚙️ Настройки", callback_data="setting"))
    return buillder.as_markup()



def settings_keybord():
    buillder = InlineKeyboardBuilder()
    buillder.add(InlineKeyboardButton(text="💭 Поменять имя", callback_data="name_change"),
                InlineKeyboardButton(text="🏠 Поменять адрес", callback_data="addresser_settings"),
                InlineKeyboardButton(text="⬅️ Вернутся", callback_data="back_to_menu"))
    
    return buillder.as_markup()
    
def addresses_keybord():
    buillder = InlineKeyboardBuilder

    buillder.add(
        InlineKeyboardButton(text="➕ ", callback_data="add_addess"),
        InlineKeyboardButton(text="⬅️ Вернутся", callback_data="back_to_menu")
    )

    buillder.adjust(1)
    return buillder.as_markup()



def back_to_menu_keyboards():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="⬅️ Вернутся", callback_data="back_to_menu"))
    return builder.as_markup()



def catalogue_keybord(wares):
    bullder = InlineKeyboardBuilder()

    for ware in wares:
        bullder.add(InlineKeyboardButton(text=ware.name, callback_data=f'ware_{ware.id}'))

    bullder.add(InlineKeyboardButton(text='⬅️ Вернутся', callback_data='back_to_menu'))
    bullder.adjust(1)
    return bullder.as_markup()



def item_keyboard():
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(text="⬅️ Вернутся", callback_data="back_to_catalogue"))
    
    return builder.as_markup()