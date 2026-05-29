import asyncio
#!/usr/bin/env python3
import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_LINK = "https://t.me/+RsMmcyN2Gqk3MWU1"

WELCOME_TEXT = """👋 Welcome to Trade with DK!

📈 Learn how to read charts, understand price movement, and make smarter trading decisions.

🎯 What you will get:
• Daily chart analysis & trade setups
• Technical analysis made simple
• Price action & trend strategies
• Risk management tips

🔥 100% Free Educational Content

Join our community now and start your trading journey today! 👇"""

HELP_TEXT = """🛠 Trade with DK — Help

This bot is your gateway to free trading education.

📌 Commands:
/start — Main menu
/help — This message
/join — Join our channel
/learn — Free learning material

📢 Our channel is updated daily with:
• Live chart breakdowns
• Market analysis
• Trade setups & signals education

👇 Join now and never miss an update!"""

LEARN_TEXT = """📚 Free Trading Education

🔰 Beginner:
• Candlestick chart basics
• Support & Resistance
• Trend identification

📊 Intermediate:
• Chart patterns
• Price action trading
• Volume analysis

🚀 Advanced:
• Smart Money Concepts
• Multi-timeframe analysis
• Risk & money management

🎯 All lessons are shared daily in our channel. Join now to access everything for FREE! 👇"""

def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Join Our Channel — FREE", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📚 Free Learning Material", callback_data="learn")],
        [InlineKeyboardButton("ℹ️ About Trade with DK", callback_data="about")],
    ])

def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Join Channel Now — FREE", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🔙 Back", callback_data="back_home")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_keyboard())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, reply_markup=main_keyboard())

async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(LEARN_TEXT, reply_markup=back_keyboard())

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Join Channel — It's FREE!", url=CHANNEL_LINK)],
    ])
    await update.message.reply_text(
        "📢 Join Trade with DK channel now!\n\nGet daily chart analysis, trade setups and free education — all in one place. 100% Free! 👇",
        reply_markup=kb
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "learn":
        await query.edit_message_text(LEARN_TEXT, reply_markup=back_keyboard())
    elif query.data == "about":
        about_text = """📌 About Trade with DK

Trade with DK is a free educational trading community focused on:

📊 Technical Analysis
📈 Price Action Trading
🧠 Chart Pattern Recognition
💡 Risk Management

Our mission: Help you understand markets clearly and build real trading skills — step by step.

⚠️ Remember:
Consistency is the key. Don't rush — focus on learning first, results will follow.

Join our channel for daily free content! 👇"""
        await query.edit_message_text(about_text, reply_markup=back_keyboard())
    elif query.data == "back_home":
        await query.edit_message_text(WELCOME_TEXT, reply_markup=main_keyboard())

async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Type /start to get started or join our FREE channel below! 👇",
        reply_markup=main_keyboard()
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("learn", learn))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))
    print("Trade with DK Bot starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
