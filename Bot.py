from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔐 Apna Bot Token daalo
BOT_TOKEN = "8401818399:AAE1sLG-NdFLdrWow9O8355bCwkAs7q8RKo"

# 🔐 Apna Telegram Chat ID (Admin ID) daalo
ADMIN_CHAT_ID = 6553817639

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
    username = f"@{user.username}" if user.username else "Not Set"
    user_id = user.id
    language_code = user.language_code or "Unknown"
    chat_type = chat.type

    # 📤 Message for User
    message = f"""
👤 <b>Telegram Details:</b>

• 🪪 <b>Full Name:</b> {full_name}
• 💬 <b>Username:</b> {username}
• 🆔 <b>User ID:</b> <code>{user_id}</code>
• 🌐 <b>Language Code:</b> {language_code}
• 💭 <b>Chat Type:</b> {chat_type}
"""
    await context.bot.send_message(chat_id=chat.id, text=message, parse_mode="HTML")

    # 📤 Message for Admin
    admin_message = f"""
📥 <b>New User Started Bot</b>

• 🪪 <b>Full Name:</b> {full_name}
• 💬 <b>Username:</b> {username}
• 🆔 <b>User ID:</b> <code>{user_id}</code>
• 🌐 <b>Language Code:</b> {language_code}
• 💭 <b>Chat Type:</b> {chat_type}
"""
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message, parse_mode="HTML")


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    app.run_polling()
