import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


# 1. जब कोई यूजर आपके स्पेशल लिंक पर क्लिक करेगा
@bot.message_handler(commands=["start"])
def send_welcome(message):
    text_parts = message.text.split() if message.text else []
    unique_code = text_parts[1] if len(text_parts) > 1 else None

    if unique_code == "math_file":
        bot.send_document(
            message.chat.id,
            "YAHAN_APNI_FILE_ID_DALEN",
            caption="📚 यहाँ आपकी मैथ की फाइल है!",
        )
    elif unique_code == "math_video":
        bot.send_video(
            message.chat.id,
            "YAHAN_APNI_VIDEO_ID_DALEN",
            caption="🎬 यहाँ आपका मैथ का वीडियो लेक्चर है!",
        )
    else:
        bot.reply_to(
            message,
            "नमस्ते! इस बॉट में आपका स्वागत है। फाइल या वीडियो पाने के लिए सही लिंक पर क्लिक करें।",
        )


# 2. जब आप बॉट को कोई फाइल या वीडियो भेजेंगे/फॉरवर्ड करेंगे, तो यह आपको उसकी File ID देगा
@bot.message_handler(content_types=["document", "video"])
def get_file_id(message):
    if message.document:
        bot.reply_to(
            message,
            f"📋 आपकी फाइल की ID यह है:\n\n`{message.document.file_id}`\n\nइसे कॉपी कर लें।",
            parse_mode="Markdown",
        )
    elif message.video:
        bot.reply_to(
            message,
            f"🎬 आपकी वीडियो की ID यह है:\n\n`{message.video.file_id}`\n\nइसे कॉपी कर लें।",
            parse_mode="Markdown",
        )
