from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator
import os

TOKEN = os.getenv("BOT_TOKEN")

async def traducir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        texto = update.message.text

        if not texto:
            return

        traduccion = GoogleTranslator(
            source='es',
            target='pt'
        ).translate(texto)

        await update.message.reply_text(
            f"🇧🇷 {traduccion}"
        )

    except Exception as e:
        print(e)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            traducir
        )
    )

    app.run_polling()

if __name__ == "__main__":
    main()
