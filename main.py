from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from random import randint, choice
import bot_msg

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
async def start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

async def help_command(msg: Message):
    await msg.answer('Сейчас я не могу помочь, так как раздел не создан')

async def send_file(msg: Message):
    await msg.answer('Кнопка находится в стадии разработки')


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def sticker_echo(msg: Message):
    print(msg.sticker.file_id)
    await msg.answer_sticker(sticker = bot_msg.random_stickers[randint(1, 8)])


# Этот хэндлер будет срабатывать на отправку стикеров
#async def send_sticker_echo(message: Message):
 #   await message.answer_sticker(message.sticker.file_id)

#@dp.message()
async def all_echo(msg: Message):
    name = msg.from_user.first_name
    await msg.answer(f'{name}, {bot_msg.bot_text[(randint(1, 5))]}')

# Регистрируем хэндлеры
dp.message.register(start_command, Command(commands=["start"]))
dp.message.register(help_command, Command('help'))
dp.message.register(send_file, Command('sendfile'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(sticker_echo, F.sticker)
dp.message.register(all_echo)

dp.run_polling(bot)

