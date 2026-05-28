import asyncio
#!/usr/bin/env python3
import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
COMMUNITY_LINK = "https://t.me/+RsMmcyN2Gqk3MWU1"

WELCOME_TEXT = """Hi 👋

I'm here to help you understand how binary markets really work through technical analysis, chart patterns, and market insights.

📊 Learn price movement
📈 Understand trends & timing
🧠 Build strong trading fundamentals

Make sure to explore the content and start learning today 👇

🔔 """ + COMMUNITY_LINK + """
🔔 """ + COMMUNITY_LINK + """
🔔 """ + COMMUNITY_LINK + """
🔔 """ + COMMUNITY_LINK + """
🔔 """ + COMMUNITY_LINK + """
🔔 """ + COMMUNITY_LINK + """

❗ IMPORTANT:
Consistency is the key. Don't rush — focus on learning first, results will follow."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))
    print("Bot starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
