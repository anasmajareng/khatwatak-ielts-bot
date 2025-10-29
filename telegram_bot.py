from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputFile

TG_BOT_TOKEN = os.environ.get("8200974660:AAFAerLQ5x5CZ5A4CA2tPCjUMQIejxifc7g")
if not TG_BOT_TOKEN:
    raise RuntimeError("TG_BOT_TOKEN environment variable is not set")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(BASE_DIR, "edited_video_intro3.mp4")
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s - %(message)s")
logger = logging.getLogger(__name__)



async def help(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "اهلا فيك بخطوتك للايلتس, المكان الاول والاخير اللي تحتاجه لتحقيق نجاحك في اختبار الايلتس, للبدء اضغط على /start")

async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):
    text = "أهلاً فيك 👋\n"
    "أنا أنس، حاصل على درجة 8 في اختبار الـ IELTS 🎯\n"
    "صممت هالبوت عشان يساعدك تحقق أفضل نتيجة خطوة بخطوة 💪\n\n"
    " من خلال هذا البوت، تقدر:\n  "
    "📘 تشوف الكورسات المتاحة لتقوية مهاراتك الأربعة (الاستماع، القراءة، الكتابة، التحدث)\n"
    "🎥 تشاهد فيديو تعريفي عن طريقة الدراسة والمحتوى\n"
    "🗣 تحجز جلسة محادثة مباشرة معي عبر Zoom\n"
    "📞 تتواصل معي مباشرة إذا عندك أي سؤال\n\n"
    "اختر أحد الأزرار بالأسفل لتبدأ 👇"
    keyboard = [
        [KeyboardButton('Courses | الكورسات'), KeyboardButton('Introductory Video | فيديو تعريفي')],     # كورسات - فيديو تعريفي
        [KeyboardButton('Speaking | محادثة'), KeyboardButton('Contact | تواصل')]   # جلسات محادثة - تواصل
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)


async def courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📘 تفاصيل الكورسات المتاحة\n\n"
        "إذا كنت فعلاً ناوي تحقق أفضل نتيجة في اختبار الـ IELTS، فهذول الكورسين صُمموا خصيصاً لإيصالك لهدفك خطوة بخطوة 💪\n\n"
        
        "🎯الكورسات المنفصلة (Recorded Courses):\n"
        "في هالكورسات، رح تلاقي كل المهارات الأساسية مقسّمة بطريقة منظمة وسهلة، بحيث تتعلم كل قسم لوحده:\n"
        "• 7 مقاطع لتدريبك على قسم الاستماع (Listening)  فيها شرح لأنواع الأسئلة، استراتيجيات الحل، وطريقة التعامل مع المقاطع الصوتية بسرعة ودقة.\n"
        "• 7 مقاطع لقسم القراءة (Reading)  تتعلّم فيها كيف تميّز الأفكار الرئيسية، تدير وقتك، وتتعامل مع الأسئلة المتشابهة والمُخادعة.\n"
        "• 7 مقاطع لقسم الكتابة (Writing)  أشرح فيها بالتفصيل طريقة كتابة الـ Task 1 والـ Task 2، مع قوالب جاهزة واستراتيجيات لرفع درجتك.\n"
        "• 5 مقاطع لقسم المحادثة (Speaking)  تتدرب فيها على الإجابة بثقة، وكيف تبني أفكارك بسرعة أثناء التحدث.\n\n"
        "كل كورس من هذول الكورسات فيه أمثلة عملية، ونماذج حقيقية من اختبارات سابقة، مع شرح دقيق لطريقة الإجابة اللي بتخلي الممتحن يعطيك أعلى درجة ممكنة.\n\n"
        
        "💻 الكورس المباشر (Live Comprehensive Course):\n"
        "أما إذا بتحب تتعلم معي بشكل مباشر وتفاعلي، فالكورس الشامل المباشر هو خيارك المثالي.\n"
        "الكورس بيتضمن جميع أقسام الـ IELTS الأربعة وبيتم بالكامل عبر Zoom بجدول منظم.\n"
        "خلال الجلسات رح أشرحلك كل قسم خطوة بخطوة، أجاوب على أسئلتك مباشرة، ونتدرب سوا على نماذج واقعية.\n\n"
        "🎓 الهدف من الكورس المباشر هو إنك تطلع من الدورة جاهز تماماً للامتحان، فاهم كل جزء من الاختبار، وعندك خطة واضحة للنجاح.\n\n"
        "اختر الطريقة اللي بتناسبك أكثر — سواء كنت بتحب تتعلّم بنفسك عبر الفيديوهات، أو تفضل التدريب المباشر معي شخصياً. في الحالتين، رح تكون أقرب بدرجة كبيرة لهدفك 💫"
    )
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    




async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Courses | الكورسات":
        await courses(update, context)

    elif text == "Introductory Video | فيديو تعريفي":
        chat_id = update.effective_chat.id 
        if not os.path.exists(video_path):
            logger.warning("Video is not found at path: %s", video_path)
            await context.bot.send_message(chat_id = chat_id, text = "الفيديو سيضاف قريبا")
            return
        try:
            with open(video_path, "rb") as video_file:
                await context.bot.send_video(
                    chat_id=chat_id,
                    video=video_file,
                    caption="🎬 الفيديو التعريفي لخطوتك للايلتس",
                    supports_streaming=True
                )
        except Exception as e:
            logger.error("Failed to send video: %s", str(e))
            await context.bot.send_message(chat_id=chat_id, text="حدث خطأ أثناء إرسال الفيديو.")
        return
        

    
    elif text == "Speaking | محادثة":
        await update.message.reply_text(" 🗣 احجز جلسة محادثة مباشرة معي عبر Zoom لتدرب على قسم التحدث بشكل عملي.\n"
        "تواصل معي عبر التيلجرام @khatwatak_ielts")
    elif text == "Contact | تواصل":
        await update.message.reply_text("📞 للتواصل المباشر معي، راسلني على تيليجرام: @khatwatak_ielts")
    else:
        await update.message.reply_text("اختر أحد الخيارات من الأزرار بالأسفل 👇")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TG_BOT_TOKEN).build()
    print("Video absolute path:", video_path)

    # Command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('courses', courses))  

    # Message handler for keyboard buttons and other texts (but not commands)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Bot started; running polling...")
    application.run_polling()
   
    

    

