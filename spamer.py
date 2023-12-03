from aiogram import Bot, Dispatcher, types, executor 
import asyncio

token = '6790829496:AAFiq3lHE6dbiuONpatrn0TZzEVJ5gXyEuA'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'spam'])
async def start(message: types.Message):
    global spam_message
    if message.text.lower().startswith('/start'):
        await message.answer('''Привет! Это спамер бот. Я готов тебе помочь к спаму! Просто добавь меня в админы в группы и напиши команду "/spam" в группе''')
    if message.text.lower().startswith('/spam'):
        await message.answer('''Хорошо, теперь напишите "spam!" для запуска спама''')
        spam_message = message.text 

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text_message(message: types.Message):
    global spam_message
    if spam_message and message.text.lower() == 'spam!':
        for _ in range(10):
            await bot.send_message(chat_id=message.chat.id, text='Спам текста')
            await asyncio.sleep(0.1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
