from core import Cmd
from helper import Config
import telebot


# TelBot class
class TelBot(telebot.TeleBot):
    # string bot token.
    bot_token = None
    # Cmd shell
    shell = None
    # Config config
    config = None

    # construct
    # string token
    def __init__(self, token):
        self.bot_token = token
        self.config = self.get_config()
        super().__init__(token)

    # get config
    # return Config
    def get_config(self):
        if self.config is None:
            self.config = Config.Config()

        return self.config

    # bot answer message
    # Message message
    def bot_answer_message(self, message):
        self.send_message(message.chat.id, "This is simple answer")

    # bot repeat message
    # Message message
    def bot_repeat_message(self, message):
        self.send_message(message.chat.id, message.text)

    # bot get shell
    # return Cmd
    def bot_get_shell(self):
        if self.shell is None:
            self.shell = Cmd.Cmd()

        return self.shell

    # bot execute shell
    # Message message
    def bot_execute_shell(self, message):
        if self.config.get_owner_id() is None or message.from_user.id != int(self.config.get_owner_id()):
            result = "Owner id is not setup or you are not owner."
        else:
            cmd = self.bot_get_shell()
            result = cmd.run_shell(message.text)

        self.send_message(message.chat.id, result)

    # bot get user id
    # Message message
    def bot_get_user_id(self, message):
        self.send_message(message.from_user.id, message.from_user.id)
