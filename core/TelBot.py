from core import config
import telebot, os, openai


class TelBot(telebot.TeleBot):
    bot_token = None
    aiBot = None

    def __init__(self, token):
        # TODO replace conf_dict var by dic()
        super().__init__(token)
        openai.organization = 'org-CA2B2JDaquhonbY6Gn2YLiqO'
        openai.api_key = "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"
        openai.Model.list()

    def bot_answer_message(self, message):
        answer = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        print(answer)
        self.send_message(message.chat.id, answer.choices[0].message.content)
    def bot_repeat_message(self, message):
        self.send_message(message.chat.id, message.text)
