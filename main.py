import asyncio
from aiogram.utils import executor
from confing import dp
import logging
from handleers import client, colback, extra, admin, fsmAdminMentor, notifications
from database.bot_db import sql_create
from database import bot_db
import  asyncio

async def on_startup(_):
    sql_create()

fsmAdminMentor.register_handlers_fsm_anketa(dp)
client.regiter_handler_client(dp)
colback.register_handler_callback(dp)
admin.register_handler_admin(dp)
bot_db.register_handlers_bot_db(dp)
notifications.register_handlers_notification(dp)
extra.register_handler_extra(dp)


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
