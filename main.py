from core import TelBot
from helper import Config

# TODO change telbot init api into api in init function
# var Telebot.
bot = TelBot.TelBot(Config.Config.static_get_bot_api())

# function cmd event.
@bot.message_handler(commands=["cmd"])
def bot_cmd_command(message):
    bot.bot_execute_shell(message)


# function get use id event.
@bot.message_handler(commands=["myid"])
def bot_get_user_id(message):
    bot.bot_get_user_id(message)


# function input text event
@bot.message_handler(content_types=["text"])
def event_bot_cont_text(message):
    bot.bot_answer_message(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
