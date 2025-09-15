from telegram import Update
from telegram.ext import ContextTypes
from data_manager import Member_State as MS
from utils import is_admin
import  datetime
from zoneinfo import ZoneInfo
import logging




async def weekly_remender(update: Update,context : ContextTypes.DEFAULT_TYPE):
    job = context.job
    chat_id = job.chat_id
    message_text = "🔔 تذكير: النهاردة يوم 📝 التوثيق الأسبوعي 📅"
    sent_message = await context.bot.send_message(
                            chat_id=chat_id,
                            text=message_text
                        )
    await context.bot.pin_chat_message(
                        chat_id=chat_id,
                        message_id=sent_message.message_id,
                        disable_notification=True)
    logging.info("weekly_remender job is done")

async def set_remender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    if await is_admin(update, context, user_id):                       
        context.job_queue.run_daily(                        
            weekly_remender,            
            time=datetime.time(tzinfo=ZoneInfo("Africa/Cairo")),  
            days=(4,),  
            name="set_remender",                   
            chat_id=chat_id,        
        )
        logging.info("weekly_remender job is added")
        await update.message.reply_text("remender started")
    else:
        await update.message.reply_text("❌ ليس لديك صلاحية")
