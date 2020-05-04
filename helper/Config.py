from config import config


# class Config
class Config:
    # construct
    def __init__(self):
        self.bot_api = config.api_key
        self.owner_id = config.owner_id
        self.help_info = config.help_methods

    # get bot api
    # return string|None
    def get_bot_api(self):
        return self.bot_api

    # static method get bot api
    # return string|None
    @staticmethod
    def static_get_bot_api():
        return config.api_key

    # get owner id
    # return string|None
    def get_owner_id(self):
        return self.owner_id

    # get help info
    # return dictinary
    def get_help_info(self):
        return self.help_info
