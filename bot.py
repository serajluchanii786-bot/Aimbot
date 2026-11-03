
import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
UPI_ID = "seraj786@upi"

PLANS = {
    "1day": {"name": "1 Day", "price": 99},
    "3day": {"name": "3 Days", "price": 199},
    "7day": {"name": "7 Days", "price": 399},
}

async def start(update, context):
    buttons = []
    for k, v in PLANS.items():
        buttons.append([InlineKeyboardButton(f"🔥 {v['name']} - Rs.{v['price']}", callback_data=k)])
    markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(f"🔥 AIM AI Premium Plans\n\nSelect your plan below:", reply_markup=markup)

async def buy(update, context):
    q = update.callback_query
    await q.answer()
    p = PLANS[q.data]
    await q.edit_message_text(f"✅ {p['name']} Selected\n\nPrice: Rs.{p['price']}\nUPI: {UPI_ID}\n\nPay and send screenshot to admin.")

flask_app = Flask(__name__)
@flask_app.route('/')
def home():
    return "BOT IS LIVE"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host='0.0.0.0', port=port)

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buy))
    print("BOT STARTED")
    app.run_polling()

if __name__ == "__main__":
    main()
