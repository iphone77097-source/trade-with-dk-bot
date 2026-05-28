#!/usr/bin/env python3
import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
COMMUNITY_LINK = "https://t.me/+RsMmcyN2Gqk3MWU1"
CHANNEL_LINK = "https://t.me/+7yojrr61-JE0OWJl"

WELCOME_TEXT = """👋 Hi! Welcome to Trade with DK

I'm here to help you understand how binary markets really work through technical analysis, chart patterns, and market insights.

📊 Learn price movement
📈 Understand trends and timing
🧠 Build strong trading fundamentals

Join our educational community and start learning today!"""

def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Join Community", url=COMMUNITY_LINK),
         InlineKeyboardButton("📣 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📚 Learn", callback_data="learn"),
         InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🛠 Help", callback_data="help")],
    ])

def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="back_home")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_keyboard())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Commands:\n\n/start - Welcome\n/help - Commands\n/about - About us\n/join - Community"
    await update.message.reply_text(text, reply_markup=main_keyboard())

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Trade with DK\n\nBinary markets education platform.\n\nConsistency is key. Learn first, results will follow!"
    await update.message.reply_text(text, reply_markup=back_keyboard())

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Join Community", url=COMMUNITY_LINK)],
        [InlineKeyboardButton("📣 Join Channel", url=CHANNEL_LINK)],
    ])
    await update.message.reply_text("Join Trade with DK community:", reply_markup=kb)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "help":
        await query.edit_message_text("Commands:\n\n/start\n/help\n/about\n/join", reply_markup=back_keyboard())
    elif query.data == "about":
        await query.edit_message_text("Trade with DK\n\nBinary markets education platform.\n\nConsistency is key!", reply_markup=back_keyboard())
    elif query.data == "learn":
        await query.edit_message_text("Learning Topics:\n\n📊 Price movement\n📈 Trends and timing\n🧠 Chart patterns\n💡 Risk management", reply_markup=back_keyboard())
    elif query.data == "back_home":
        await query.edit_message_text(WELCOME_TEXT, reply_markup=main_keyboard())

async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Type /start or /help to see commands!", reply_markup=main_keyboard())

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))
    print("Bot starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
