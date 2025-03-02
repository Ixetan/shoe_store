from aiogram.fsm.state import State,  StatesGroup

class SettingsStates(StatesGroup):
    choose_name = State()
    address_label = State()
    add_address_text = State()