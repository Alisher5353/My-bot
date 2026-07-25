from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = "8636704367:AAHNF3cNadFMi_763m81BGca27OXD0EN29U"
KANAL_USERNAME = "ali_bagatiy" # @ belgisiz yozing


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "📢 Kanalga qo'shilish",
                url=f"https://t.me/{KANAL_USERNAME}"
            )
        ],
        [
            InlineKeyboardButton(
                "✅ Qo'shildim",
                callback_data="check_sub"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            "👋 Assalomu alaykum!\n\nBotdan foydalanish uchun avval kanalga qo'shiling.",
            reply_markup=reply_markup
        )


async def check_sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(
            chat_id=f"@{KANAL_USERNAME}",
            user_id=user_id
        )

        if member.status in ["member", "administrator", "creator"]:
            await query.edit_message_text(
                "✅ Tabriklaymiz! Siz kanalga qo'shilgansiz.\n\nEndi botdan foydalanishingiz mumkin."
            )
        else:
            await query.answer(
                "❌ Avval kanalga qo'shiling!",
                show_alert=True
            )

    except Exception:
        await query.answer(
            "❌ Bot kanalni tekshira olmadi. Botni kanalga admin qiling.",
            show_alert=True
        )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check_sub, pattern="check_sub"))

print("Bot ishga tushdi...")
app.run_polling()