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


@bot.message_handler(commands=["weather"])
def bot_weather(message):
    bot.bot_get_weather(message)


@bot.message_handler(commands=["camscreen"])
def bot_cmd_camshot(message):
    bot.send_message(message.from_user.id, cmd.make_fast_camshot(message))


# function get use id event.
@bot.message_handler(commands=["myid"])
def bot_get_user_id(message):
    bot.send_message(message.from_user.id, bot_functions.function_get_user_id(message))


# function input text event
@bot.message_handler(content_types=["text"])
def event_bot_cont_text(message):
    bot.bot_answer_message(message)


@bot.message_handler(commands=["botimg"])
def event_bot_image_g(message):
    bot.bot_generate_image(message)


# TODO fix photo problems
# function input text event
@bot.message_handler(func=lambda message: True, content_types=["photo", "new_chat_photo"])
def event_bot_cont_photo(message):
    bot.bot_photo(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
