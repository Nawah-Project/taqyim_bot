from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters,InlineQueryHandler
import os
from dotenv import load_dotenv
import logging
from commands.massage_handler import monitoring_topic , new_user
from commands.set_timer import set_timer
from commands.set_remender import set_remender

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


# إعداد أساسي
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# اسكت المكتبات الخارجية
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


app = ApplicationBuilder().token(BOT_TOKEN).build()

async def state(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    await update.message.reply_text(f"{chat_id}{user_id}")


app.add_handler(CommandHandler('set_timer', set_timer))
app.add_handler(CommandHandler('set_remender', set_remender))

app.add_handler(MessageHandler(filters.ChatType.GROUPS & filters.StatusUpdate.NEW_CHAT_MEMBERS, new_user))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitoring_topic))


app.run_polling()