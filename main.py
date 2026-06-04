import os
import telebot

# यह लाइन सर्वर से आपका छुपा हुआ टोकन उठाएगी
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


# जब कोई /start या आपके लिंक पर क्लिक करेगा
@bot.message_handler(commands=["start"])
def send_welcome(message):
    # लिंक के पीछे का कोड अलग करना
    text_parts = message.text.split()
    unique_code = text_parts[1] if len(text_parts) > 1 else None

    if unique_code == "math_book_101":
        bot.reply_to(
            message,
            "📚 नमस्ते! यह आपकी Class 10th की मैथ्स बुक का डाउनलोड लिंक है: [यहाँ क्लिक करें](https://example.com)",
            parse_mode="Markdown",
        )
    elif unique_code == "science_notes":
        bot.reply_to(
            message, "📝 यहाँ आपके साइंस के शॉर्ट नोट्स की फाइल है!"
        )
    else:
        bot.reply_to(
            message,
            "नमस्ते! इस बॉट में आपका स्वागत है। कोई स्पेशल कोड नहीं मिला।",
        )
        
        
