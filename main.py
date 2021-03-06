import sys
from core import cmd, charles_bot, bot_functions, config, TelBot

# TODO: change this check to another, maybe in bot
if config.api_key is None:
    exit('Please insert api key in project_root/core/config::api_key')

# var Telebot.
bot = TelBot.TelBot(config.api_key)

# function help event.
@bot.message_handler(commands=["help"])
def bot_help_command(message):
    bot.send_message(message.chat.id, bot_functions.function_get_help_info())


# function cmd event.
@bot.message_handler(commands=["cmd"])
def bot_cmd_command(message):
    bot.send_message(message.chat.id, cmd.function_cmd_start(message))


# function get use id event.
@bot.message_handler(commands=["myid"])
def bot_get_user_id(message):
    bot.send_message(message.from_user.id, bot_functions.function_get_user_id(message))


# function input text event
@bot.message_handler(content_types=["text"])
def event_bot_cont_text(message):
    bot.bot_answer_message(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
