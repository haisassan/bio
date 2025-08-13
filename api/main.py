from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest  # Импортируем UpdateProfileRequest
import schedule
import time
import datetime
import asyncio

# Замените на свои значения
api_id = 24337505  #  Ваш api_id
api_hash = '5fd83d69d3e6ad61f50ba4948e7f4150'  # Ваш api_hash
phone_number = '+79388657518'  # Ваш номер телефона (с кодом страны)
descriptions = [
    "one day I am gonna grow wings",
    "just call me mr.modest, I got it and flaunt it",
    "are you sick of me? Would you like to be?",
    "oh the boy a slag, the best you ever had",
    "but heaven knows, I'm miserable now",
    "she looks like a real thing. she tastes like a real thing",
    "it wears me out",
    "I think you should know - you his favourite worst nightmare",
    "no alarms and no surprises",
    "we're fated to pretend",
    "you look like you've been a breakfast at a heartbreak hotel",
    "so if you lonely, you know I'm here waiting for you",
    "well, see you later, innovator",
    "you do it to yourself, you do, and that's what really hurts",
    "cause all the fools on parade, cavort and carry on for waiting eyes",
    "you know where to find me, and I know where to look",
    "the winner takes it all",
    "I don't wanna die, I sometimes wish i'd never been born at all",
    "wisdom choke you",
    "take it easy for a little while",
    "that's because I'm a good old-fashioned loverboy",
    "Karma police, arrest this man - he talks in maths",
    "another one bites the dust",
    "just as you take my hand, just as you write my number down"
]

client = TelegramClient('session_name', api_id, api_hash)  # 'session_name' - имя файла, в котором будут храниться данные сессии

async def change_bio():
    """Изменяет описание профиля."""
    try:
        now = datetime.datetime.now()
        index = now.day % len(descriptions) # Используем день месяца для выбора описания
        new_bio = descriptions[index]

        await client(UpdateProfileRequest(about=new_bio))  # Используем UpdateProfileRequest
        print(f"Описание изменено на: {new_bio}")
    except Exception as e:
        print(f"Ошибка при изменении описания: {e}")

async def run_change_bio():
    """Запускает асинхронную функцию изменения описания."""
    try:
        async with client:
            await change_bio()
    except Exception as e:
        print(f"Ошибка в run_change_bio: {e}")

# Укажите время, когда нужно менять описание (в 24-часовом формате, например, '10:00')
change_time = '16:40'  # Меняйте на желаемое время

def schedule_change_bio():
    asyncio.create_task(run_change_bio())


schedule.every().day.at(change_time).do(schedule_change_bio)


async def main():
    """Основная функция для запуска клиента и проверки авторизации."""
    await client.start(phone=phone_number)  # Запускаем клиент и запрашиваем авторизацию, если необходимо
    print("Telegram клиент запущен. Ожидание запланированных изменений описания.")

    #  Проверяем, авторизован ли клиент
    if not await client.is_user_authorized():
        print("Пожалуйста, авторизуйтесь в Telegram.")
        return

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

