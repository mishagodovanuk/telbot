from core import config, charles_bot
import apiai, json, pprint

# var Telebot.
bot_charles = charles_bot.bot


# function bot hello.
def function_bot_hello(message):
    bot_charles.send_message(
        message.chat.id,
        "Hello " + message.from_user.first_name + " we will send you answer as soon as posible"
    )


# function bot repeat.
def function_bot_repeat(message):
    bot_charles.send_message(message.chat.id, message.text)


# function bot send user data.
def function_bot_send_user_data(message, send_to=None):
    if send_to is None:
        send_to = config.owner_id

    bot_charles.send_message(
        send_to,
        "Usename:" + message.from_user.first_name + "\n"
        + "User id:" + str(message.from_user.id) + "\n"
        + "Text:" + message.text
    )


# function get user id.
def function_get_user_id(message):
    return message.from_user.id


# function get help info all.
def function_get_help_info():
    result = ''
    for key in config.help_methods:
        result += key + ": " + config.help_methods[key] + "\n"

    return result


# function bot say.
# use google dialogflow.
def function_bot_say(message):
    request = apiai.ApiAI(config.apiai_api_key).text_request()
    request.lang = config.lang_default
    request.session_id = message.chat.id
    request.query = message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    pprint.pprint(responseJson)
    response = responseJson['result']['fulfillment']['speech']
    if response:
        return response
    else:
        return "Повторіть"
