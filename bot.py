import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Fazer Exercício 🎯", callback_data="exercise")],
        [InlineKeyboardButton("Dica de Inglês 💡", callback_data="tip")],
        [InlineKeyboardButton("Aulas com o Professor 👨‍🏫", callback_data="sales")]
    ]
    await update.message.reply_text(
        "Olá! Eu sou o *JV Speak Bot* 🇬🇧\n\nComo posso te ajudar hoje?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    if data == "exercise":
        await query.message.reply_text("Traduza para o português:\n\n*“I’m looking forward to meeting you.”*")
    elif data == "tip":
        await query.message.reply_text("💡 Dica: 'Looking forward to' SEMPRE vem seguido de verbo com ING!")
    elif data == "sales":
        await query.message.reply_text(
            "👨‍🏫 *Aulas com o Professor Victor*\n\n"
            "✔ Conversação real\n"
            "✔ Correções ao vivo\n"
            "✔ Material incluído\n\n"
            "Quer conhecer os planos?"
        )
    await query.answer()

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "looking forward to meeting you" in text:
        await update.message.reply_text("Perfeito! 👏 Tradução correta!")
        return
    await update.message.reply_text("Ainda não entendi 😅\nUse /start para ver as opções!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
