from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Define your bot token here
Token = "7363259019:AAGkKvkNaXleroSmGadugTm5iFGKg7afid4"

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hii.. Welcome to the Simplilearn Playlist Bot! "
                                     "Use /help to see available commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
/start - Start the bot 
/help -  This help message
/content - Info about various playlists of Simplilearn
/python - Playlist for Python
/sql - Playlist for SQL
/ai - Playlist for AI
/ml - Playlist for Machine Learning
/java - Playlist for Java
/contact - Contact details
/about - About this bot
/feedback - Provide feedback
""")

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is some information about various playlists of Simplilearn:")

async def python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://youtu.be/t2_Q2BRzeEE?si=ztWqI_ynIAaWNBou")

async def sql(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://www.youtube.com/live/q_JsgpiuY98?si=lk9HdNfG54Yu2heL")

async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://youtu.be/HfRwJFk66dc?si=G_JNAA5ThUCWfo6l")

async def ml(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://youtu.be/LvC68w9JS4Y?si=zG7oA0nQK-cF8lQc")

async def java(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://youtu.be/PymbRTMb4hY?si=-WBauR-5O6wzmjVE")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can contact on the registered email ID provided on the website.")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This bot provides Simplilearn playlists and assists users with their queries.")

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("We appreciate your feedback! Please type your message below.")
    context.user_data['feedback'] = True

async def handle_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('feedback'):
        feedback_text = update.message.text
        # You can log or store feedback_text here
        await update.message.reply_text("Thank you for your feedback!")
        context.user_data['feedback'] = False
    else:
        await update.message.reply_text("Please use the /feedback command to provide feedback.")

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(Token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("content", content))
    app.add_handler(CommandHandler("python", python))
    app.add_handler(CommandHandler("sql", sql))
    app.add_handler(CommandHandler("ai", ai))
    app.add_handler(CommandHandler("ml", ml))
    app.add_handler(CommandHandler("java", java))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("feedback", feedback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_feedback))

    print("Bot is running...")
    app.run_polling()
