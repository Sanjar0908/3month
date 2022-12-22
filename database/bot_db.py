import random
import sqlite3
from  aiogram import  types, Dispatcher
# СУБД - Система управления базой данных
# SQL = Structured Query Language


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY, name TEXT, "
               "direction TEXT, age INTEGER, gruppa TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(result)
    await message.answer(f"id - {random_user[0]}\nname - {random_user[1]}\ndirection - {random_user[2]} "
                        f"age - {random_user[3]}\ngroup - {random_user[4]}"
    )


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()

def register_handlers_bot_db(dp: Dispatcher):
    dp.register_message_handler(sql_command_random, commands=['random'])

