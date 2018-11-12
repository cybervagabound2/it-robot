from telegram import ReplyKeyboardMarkup
import database.users
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    user = add_user(update)
    reply_keyboard = ReplyKeyboardMarkup([
        ['📚 Библиотека', '🐧 Linux'],
        ['💻 Программирование', '🌐 Blockchain'],
        ['🗂 Каналы', '🗣 Чаты']
    ])
    update.message.reply_text('Добро пожаловать в it-робота. Здесь ты найдешь все , что необходимо',
                              reply_markup=reply_keyboard)


def add_user(update):
    dbusers = database.users.DbUsers()
    user = dbusers.get_single(user_id=update.message.from_user.id)
    if user == None:
        new_user = []
        new_user.append(update.message.from_user.id)
        new_user.append(update.message.chat.username)
        new_user.append(update.message.chat.first_name)
        new_user.append(update.message.chat.last_name)
        new_user.append('/start')
        dbusers.add_new(new_user)
    else:
        pass
        #bot.send_message(chat_id=523792555, text='error add start.py/add_user')
