from core import config
import telebot


class TelBot(telebot.TeleBot):
    bot_token = None

    def __init__(self, token):
        # TODO replace conf_dict var by dic()
        super().__init__(token)

    def bot_answer_message(self, message):
        self.send_message(message.chat.id, "This is simple answer")

    def bot_repeat_message(self, message):
        self.send_message(message.chat.id, message.text)
