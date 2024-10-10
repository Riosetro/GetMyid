from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Функция для отображения User ID и Chat ID
async def start(update: Update, context):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    
    # Кнопки для копирования User ID и Chat ID
    keyboard = [
        [
            InlineKeyboardButton(f"Copy User ID: {user_id}", callback_data=f"user_id_{user_id}"),
            InlineKeyboardButton(f"Copy Chat ID: {chat_id}", callback_data=f"chat_id_{chat_id}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"Your User ID: `{user_id}`\nYour Chat ID: `{chat_id}`", 
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Обработчик нажатия кнопок для копирования
async def button_click(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data.startswith('user_id'):
        await query.message.reply_text(f"User ID `{query.data.split('_')[1]}` copied!", parse_mode='Markdown')
    elif query.data.startswith('chat_id'):
        await query.message.reply_text(f"Chat ID `{query.data.split('_')[1]}` copied!", parse_mode='Markdown')

# Функция для /help на двух языках
async def help_command(update: Update, context):
    # Получаем язык пользователя
    user_lang = update.effective_user.language_code
    if user_lang == 'ru':
        help_text = (
            "Привет! Вот как ты можешь использовать этого бота:\n\n"
            "1. Команда /start покажет твой User ID и Chat ID.\n"
            "2. Нажми на кнопки, чтобы скопировать ID.\n"
            "Для чего это нужно?\n"
            "User ID используется для идентификации тебя как пользователя.\n"
            "Chat ID нужен для отправки сообщений в конкретный чат.\n\n"
            "Больше информации: [Telegram API Documentation](https://core.telegram.org/bots/api#user)"
        )
    else:
        help_text = (
            "Hello! Here's how to use this bot:\n\n"
            "1. The /start command will show you your User ID and Chat ID.\n"
            "2. Click the buttons to copy the IDs.\n"
            "Why do you need this?\n"
            "User ID is used to identify you as a user.\n"
            "Chat ID is needed to send messages to a specific chat.\n\n"
            "More info: [Telegram API Documentation](https://core.telegram.org/bots/api#user)"
        )
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

# Основной код для запуска бота
if __name__ == '__main__':
    application = ApplicationBuilder().token("7750349163:AAGUuy4_JXqDYYe4uBbutdNEtrK9nthYsMc").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button_click))

    application.run_polling()
