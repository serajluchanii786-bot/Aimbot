import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
UPI_ID = "seraj786@upi"

PLANS = {
  "1day": {"name": "1 Day", "price": 99},
  "3day": {"name": "3 Days", "price": 199},
  "7day": {"name": "7 Days", "price": 399},
}

async def start(update, context):
    buttons = []
    for k,v in PLANS.items():
        buttons.append([InlineKeyboardButton(f"{v['name']} - Rs {v['price']}", callback_data=k)])
    await update.message.reply_text("🔥 AIM AI GLOBAL CLONE BOT\nPlan select karo:", reply_markup=InlineKeyboardMarkup(buttons))

async def buy(update, context):
    q = update.callback_query
    await q.answer()
    p = PLANS[q.data]
    await q.edit_message_text(f"✅ {p['name']} Selected\nPrice: {p['price']}\nPay to: {UPI_ID}\nScreenshot bhejo.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buy))
    print("BOT STARTED")
    app.run_polling()

if __name__ == "__main__":
    main()
