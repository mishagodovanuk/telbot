# apiai api_key
apiai_api_key = '1504c03450fe420c932a499e1c42d05e'

# default language
lang_default = 'ru'

# bot api key
api_key = '1169105152:AAG0XnBUBGFeFr8sU554WDcyYrmKzlBBwSM'

# owner_id.
# insert owner id.
owner_id = '833026088'

# var help methods list.
help_methods = dict()

# set help methods list.
help_methods['/cmd'] = 'Command prompt (use /cmd -h for mode info)'
help_methods['/help'] = 'List of all commands1169105152:AAG0XnBUBGFeFr8sU554WDcyYrmKzlBBwSM'
help_methods['/myid'] = 'Return user id to user'


# function is owner exist.
def function_is_owner_exist():
    if owner_id is None:
        return False
    return True
