#!/usr/bin/env python3
import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
COMMUNITY_LINK = "https://t.me/+RsMmcyN2Gqk3MWU1"
CHANNEL_LINK = "https://t.me/+7yojrr61-JE0OWJl"

WELCOME_TEXT = """👋 <b>Hi! Welcome to Trade with DK</b>

I'm here to help you understand how <b>binary markets</b> really work — through technical analysis, chart patterns, and market insights.

━━━━━━━━━━━━━━━━━━━━
📊 Learn price movement
📈 Understand trends & timing
🧠 Build strong trading fundamentals
━━━━━━━━━━━━━━━━━━━━

Join our educational community and start learning today! 👇"""

def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Join Community", url=COMMUNITY_LINK), InlineKeyboardButton("📣 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📚 Learn", callback_data="learn"), InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🛠 Help", callback_data="help")],
    ])

def back_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back_home")]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(WELCOME_TEXT, reply_markup=main_keyboard())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("🛠 <b>Commands:</b>\n\n/start - Welcome\n/help - Commands\n/about - About us\n/join - Community links", reply_markup=main_keyboard())

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("📌 <b>Trade with DK</b>\n\nBinary markets education platform.\n\n⚠️ Consistency is key. Learn first, results will follow!", reply_markup=back_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "help":
        await query.edit_message_text("🛠 <b>Commands:</b>\n\n/start\n/help\n/about\n/join", parse_mode="HTML", reply_markup=back_keyboard())
    elif query.data == "about":
        await query.edit_message_text("📌 <b>Trade with DK</b>\n\nBinary markets education platform.\n\n⚠️ Consistency is key!", parse_mode="HTML", reply_markup=back_keyboard())
    elif query.data == "learn":
        await query.edit_message_text("📚 <b>Learning Topics:</b>\n\n📊 Price movement\n📈 Trends & timing\n🧠 Chart patterns\n💡 Risk management", parse_mode="HTML", reply_markup=back_keyboard())
    elif query.data == "back_home":
        await query.edit_message_text(WELCOME_TEXT, parse_mode="HTML", reply_markup=main_keyboard())

async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("🤔 /start likho ya /help dekho!", reply_markup=main_keyboard())

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))
    print("🚀 Bot chal raha hai...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
