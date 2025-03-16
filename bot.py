import asyncio
from email import message
from aiogram import F, Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext

from dotenv import dotenv_values
from users import address
from users.users import read_user_config, write_user_config, update_user_config, user_exists
from keyboards.keyboards import start_keybord, settings_keybord, addresses_keybord, back_to_menu_keyboards, catalogue_keybord, item_keyboard
from states.state import SettingsStates
from users.address import Address
from wares.wares import wares, Ware

config = dotenv_values()

bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()



@dp.message(Command('start'))
async def cmd_start(message: Message): 
    user = message.from_user
    user_id = user.id

    if user_exists(user_id=user_id):
        user_config = read_user_config(user_id=user_id)
    else:
        user_config = {
            "first_name": user.first_name,
            "addresses": [],
            "cashback_points": 0
        }
        write_user_config(user_id=user_id, config=user_config)
    await message.answer(f"Здраствуйте, {user_config['first_name']}",
                        reply_markup=start_keybord()
                        )



@dp.callback_query(F.data == 'setting')
async def setting_menu(callback: CallbackQuery):
    await callback.message.edit_text('Настройки акаунта',
                                     reply_markup=settings_keybord())



@dp.callback_query(F.data == 'back_to_menu')
async def back_to_menu(callback: CallbackQuery):
    user_id = callback.message.chat.id
    user = read_user_config(user_id=user_id)

    await callback.message.edit_text(text=f'Добро пожпловать в магазин обуви',
                                     reply_markup=start_keybord())



@dp.callback_query(F.data == 'name_change')
async def name_change(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Новое имя:")

    state.set_state(SettingsStates.choose_name)



@dp.message(F.text, SettingsStates.choose_name)
async def new_name(message: Message, state: FSMContext):
    new_name = message.text
    user_id = message.from_user.id

    keys_to_update = {
        'first_name': new_name
    }

    update_user_config(user_id=user_id, keys_to_update=keys_to_update)

    await message.answer(text=f'{new_name}, Новое имя',
                         reply_markup=back_to_menu_keyboards())
    await state.set_state(None)



@dp.callback_query(F.data=="addresses_settings")
async def addresses_settings(callback: CallbackQuery, state: FSMContext):
    user_id = callback.message.chat.id
    config = read_user_config(user_id=user_id)

    if len(config[address]) == 0:
        await callback.message.edit_text('У вас нет адреса.\nДобавте его ниже',
                                         reply_markup=addresses_keybord())



@dp.callback_query(F.data=='add_address')
async def add_address(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Новый адрес:")

    state.set_state(SettingsStates.address_label)



@dp.message(F.text, SettingsStates.address_label)
async def add_address_label(messahe: Message, state: FSMContext):
    address_label = message.text

    await message.answer(f'Укажите адресс для {address_label}')
    await state.set_state(SettingsStates.add_address_text)
    await state.set_data({"label": address_label})



@dp.message(F.text, SettingsStates.add_address_text)
async def add_address_text(message: Message, state: FSMContext):
    address = message.text

    date = await state.get_date()
    address_label = date('label')

    user_id = message.from_user.id
    config = read_user_config(user_id=user_id)

    new_address = Address.from_dict(
        {
            "label": address_label,
            "address": address
        }
    )

    config['addresses'].append(new_address.to_dict())
    keys_to_update = {
        'address': config['addresses']
    }
    update_user_config(user_id=user_id, keys_to_update=keys_to_update)


@dp.callback_query(F.data=='back_to_catalogue')
@dp.callback_query(F.data=='catalogue')
async def catalogue(callback: CallbackQuery, state: FSMContext):
    user_id = callback.message.chat.id
    user = read_user_config(user_id=user_id)
    name = user['first_name']
    await callback.message.edit_text(f'{name}, Выберите товар!', 
                                     reply_markup=catalogue_keybord(wares)) 



@dp.callback_query(F.data.startswith('ware_'))
async def ware_info(callback: CallbackQuery):
    ware_id = int(callback.data.split('_')[-1])
    ware: Ware = Ware.get_ware_by_id(wares, ware_id)

    #для отправки фото:
    #await callback.message.answer_photo(photo=ware.inputImage)

    await callback.message.edit_text(text=ware.get_ware_details(),
                                     reply_markup=item_keyboard())
    


async def main():
    print("Бот запушен!")
    await dp.start_polling(bot)
    
asyncio.run(main())