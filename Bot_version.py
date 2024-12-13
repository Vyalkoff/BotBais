# import requests
# import time
#
# API_URL = 'https://api.telegram.org/bot'
# API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
# BOT_TOKEN = '6048932941:AAG3bb9C8sPcZUp4KnisNBcxoMRCYtDr8z0'
# TEXT = 'Ура! Классный апдейт!'
# ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('
# MAX_COUNTER = 100
#
# offset = -1
# counter = 0
# cat_response: requests.Response
# cat_link: str
# chat_id: int
#
# while counter < MAX_COUNTER:
#
#     print('attempt =', counter)  # Чтобы видеть в консоли, что код живет
#
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_response = requests.get(API_CATS_URL)
#             if cat_response.status_code == 200:
#                 cat_link = cat_response.json()[0]['url']
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
#             else:
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
#
#     time.sleep(1)
#     counter += 1


import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from aiogram.enums.dice_emoji import DiceEmoji
# эмодзи

logging.basicConfrig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
#bot = Bot(token=)

dp = Dispatcher()


@dp.message(Command('/start'))
async def cmd_start(message: types.Message):
    await message.answer('hello')


async def main():
    await dp.start_polling(bot)
    if __name__ == '__main__':
        asyncio.run(main())
