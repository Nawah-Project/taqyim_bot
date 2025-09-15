from telegram import Update
from telegram.ext import ContextTypes
from data_manager import Member_State as MS
from utils import is_admin
import  datetime
from zoneinfo import ZoneInfo
import logging
async def weekly_check(context : ContextTypes.DEFAULT_TYPE):
    job = context.job
    chat_id = job.chat_id
    MS().weekly_missed_update(chat_id)
    logging.info("weekly_check job is done")

async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    if await is_admin(update, context, user_id):                       
        context.job_queue.run_daily(                        
            weekly_check,            
            time=datetime.time(tzinfo=ZoneInfo("Africa/Cairo")),  
            days=(6,),  
            name="set_timer",                   
            chat_id=chat_id,       
        )
        logging.info("weekly_check job is added")
        await update.message.reply_text("timer started")
    else:
        await update.message.reply_text("❌ ليس لديك صلاحية")
