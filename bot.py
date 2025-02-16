import asyncio
from aiogram import F, Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message

from dotenv import dotenv_values
from users.users import read_user_config, write_user_config
from keyboards.keyboards import start_keybord

config = dotenv_values()

bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: Message): 
    user = message.from_user
    user_id = user.id
    user_config = {
        "first_name": user.first_name,
        "addresses": [],
        "cashback_points": 0, 
    }
    write_user_config(user_id=user_id, config=user_config)
    await message.reply(f"Здраствуйте, {user.first_name}",
                        reply_markup=start_keybord()
                        )

async def main():
    print("Бот запушен!")
    await dp.start_polling(bot)
    
asyncio.run(main())