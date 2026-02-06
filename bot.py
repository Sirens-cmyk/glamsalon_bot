import sys
import types

# حل مشکل پایتون 3.13 گوشی
m = types.ModuleType("imghdr")
m.what = lambda f, h=None: None
sys.modules["imghdr"] = m

# --- ایمپورت‌های اصلاح شده ---
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7957409761:AAGIE9thRf5ogyTMt8XtzHtpA5Yobe5Z1ZE"
WEBAPP_URL = "https://sirens-cmyk.github.io/glamsalon_bot/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🌸 ورود به پنل رزرو آنلاین", web_app=WebAppInfo(url=WEBAPP_URL))]]
    await update.message.reply_text(
        "سلام! به سالن زیبایی خوش آمدید.\nبرای رزرو نوبت روی دکمه زیر بزنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # دریافت داده از مینی‌اپ
    data = update.effective_message.web_app_data.data
    await update.message.reply_text(f"✅ نوبت جدید با موفقیت ثبت شد:\n\n{data}")

if __name__ == "__main__":
    # ساخت اپلیکیشن
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # اضافه کردن دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    
    print("🚀 ربات با موفقیت در ترموکس فعال شد...")
    app.run_polling()

