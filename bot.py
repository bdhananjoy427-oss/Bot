from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

Configuration

BOT_TOKEN = "8686256029:AAE944hgQx1snAUB2ZmwFsvlPhZ2mEUhI-Q"
CHANNELS = ["@channel1", "@channel2", "@channel3", "@channel4"]
FINAL_LINK = "https://t.me/+QFxCNjGZ8QxlODA1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
user = update.effective_user
keyboard = []
for i, ch in enumerate(CHANNELS, 1):
keyboard.append([InlineKeyboardButton(f"CHANNEL {i} 🛡️", url=f"https://t.me/{ch[1:]}")])

keyboard.append([InlineKeyboardButton("CHECK JOINED ✅", callback_data="check_join")])  
reply_markup = InlineKeyboardMarkup(keyboard)  
  
await update.message.reply_text(  
    f"HELLO DEAR USER 👋🫶 {user.first_name}\n\nFIRST JOIN ALL CHANNELS THEN YOU GET THE LINK 🔗",  
    reply_markup=reply_markup  
)

async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
query = update.callback_query
user_id = query.from_user.id
missing = []

for ch in CHANNELS:  
    try:  
        member = await context.bot.get_chat_member(chat_id=ch, user_id=user_id)  
        if member.status in ['left', 'kicked', 'restricted']:  
            missing.append(ch)  
    except:  
        missing.append(ch)  

if missing:  
    msg = "YOU ARE NOT JOINED ALL CHANNELS 🚫 PLEASE JOIN ALL CHANNELS 💥\n\n" + "\n".join(missing)  
    await query.answer(text="You haven't joined all channels!", show_alert=True)  
    await query.edit_message_text(msg)  
else:  
    await query.answer(text="Successfully checked!")  
    await query.edit_message_text(f"Congratulations! You have completed all steps. Here is your link 🔗:\n{FINAL_LINK}")

if name == 'main':
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check_join, pattern="check_join"))
app.run_polling()

I want  to host this bot inrender pollaing bot  give  me a requiremennts txt