import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Jaa na Bsdk, gaand mara jaake.",
    "Tu paidaishi chutiya hai ki koi course kiya hai? ",
    "Yarr Teri kitni makhaali gaand.",
    "The world would have been so smooth if your dad had just pulled out",
    "Luli hoti ni khadi, baate karta badi badi",
    "What else can you do other than spreading your legs?",
    "Jaa na Gandu",
    "Aand ka na Gaand ka, Gyaan jhaare pure Brahmand ka",
    "Dhaat teri maa ki ch*t",
    "Gaand se tatti nikalke jaadugar samajhta hai apne aap ko?",
    "Tumhari gaand hai ya blackhole'",
    "Gaand Mai sariya daal dunga bsdk",
    "Tu aise nhi maanega - Mat maan, maa chuda",
    "Tujhse zada sundar teri jali hui gaand hai",
    "Ye aapki Randikhana nhi hai, kripya yaha se dur rahe",
    "Jyada gaand na fulao warna yhi patak ke chod denge.",
    "bsdkeee jyada na bol rha he",
    "saale gand marwa apni"
  )

@run_async
def abuse(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))


ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)

dispatcher.add_handler(ABUSE_HANDLER)
