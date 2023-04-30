from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

# бот имеет название HealthyFood, скриншоты бота расположены в папке screen_bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters

BOT_TOKEN = '6287615376:AAH5CnPPnhvY1Uuplv6lL3zOmORYIcaGx0E'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


async def echo(update, context):
    await update.message.reply_text(f'Я получил сообщение {update.message.text}')


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    text_handler = MessageHandler(filters.TEXT, echo)

    # Регистрируем обработчик в приложении.
    application.add_handler(text_handler)

    # Запускаем приложение.
    application.run_polling()


if __name__ == '__main__':
    main()
