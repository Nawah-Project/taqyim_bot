from telegram import Update
from telegram.ext import ContextTypes
from documentation import Documentation
from doc_register import doc_register
import os
from dotenv import load_dotenv
from datetime import datetime
from data_manager import Member_State




load_dotenv()
MS = Member_State()
DOCUMENT_ID = os.getenv("DOCUMENT_ID")




def create_massage(name,text):
    date = datetime.now().strftime("%Y-%m-%d")
    massage = f"📝 التوثيق الشخصي لـ {name}:\n\n{text}\n\n📅 التاريخ: {date}"
    separator = "\n___________________________________________\n"
    
    full_text_to_insert = massage + separator

    return  full_text_to_insert 


async def monitoring_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    
    monitoring_topic_id = 12
    if update.message.message_thread_id is monitoring_topic_id:
        await submit_achievement(update, context)
    

async def new_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    member_id = update.effective_user.id
    name = update.effective_user.first_name + " " + update.effective_user.last_name
    MS().check_member_id(member_id, name)
    
async def submit_achievement(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    member_id = update.effective_user.id
    
   
    if Documentation().check_documentation(update.message.text):
        if MS().get_missed(member_id) > 0:
            
            MS().update_member_missed(member_id)
           
            text = update.message.text
            name = update.effective_user.first_name + " " + update.effective_user.last_name
            massage = create_massage(name,text)
            doc_register(DOCUMENT_ID,massage)

            await update.message.delete()
        else:
            await update.message.reply_text(
                "⚠️ لقد سجّلت توثيقك هذا الأسبوع بالفعل.\n"
                "⏳ لا يمكن تسجيل أكثر من مرة في نفس الأسبوع."
            )
    else:
        await update.message.reply_text(
            "📝 تذكير مهم:\n\n"
            "المكان ده مخصص فقط لتسجيل **التوثيقات الأسبوعية** ✅\n"
            "عند إرسال التوثيق لازم تحتوي الرسالة على:\n"
            "🔹 كلمة *التوثيق الأسبوعي* أو\n"
            "🔹 كلمة *توثيق* لوحدها."
        )
