from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
TOKEN = config("TOKEN")
storage = MemoryStorage()
ADMINS = [1065345799]
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)