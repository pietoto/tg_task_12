from telegram.ext import CommandHandler, ApplicationBuilder
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import datetime
from datetime import date

BOT_TOKEN = '6287615376:AAH5CnPPnhvY1Uuplv6lL3zOmORYIcaGx0E'


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    )


async def help_command(update, context):
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


async def date_(update, context):
    d = date.today()
    await update.message.reply_text(f'{d}')


async def time_(update, context):
    t = datetime.datetime.now().time()
    await update.message.reply_text(f'{t}')


def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("date", date_))
    application.add_handler(CommandHandler("time", time_))
    application.run_polling()


if __name__ == '__main__':
    main()
