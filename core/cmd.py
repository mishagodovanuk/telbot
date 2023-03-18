from core import config
import subprocess
import os



# function cmd start.
def function_cmd_start(message):
    if message.text == '/cmd -h':
        return function_get_cmd_info()

    if not config.function_is_owner_exist():
        return "For using this please set owner id in" + os.getcwd() + "/core/config.py::owner_id"

    if message.from_user.id != int(config.owner_id):
        return "Only owner can execute shell commands."

    return function_execute_shell(message)


# function cmd execute shell.
def function_execute_shell(message):
    command = message.text.replace('/cmd', '')
    if not function_cmd_check_write(command):
        return "You cant execute all CRUID commands,only Read operations"

    shell = subprocess.run(
        command,
        shell=True,
        check=False,
        capture_output=True)
    return shell.stdout if shell.stdout else shell.stderr


# function cmd check write permission.
def function_cmd_check_write(command):
    # for element in disallowed_commands:
    #     if element in command:
    #         return False
    return True


# function get cmd info.
def function_get_cmd_info():
    return "Every commands is execute like: /cmd my command \n" \
           "For example: /cmd ll - will return list content of" \
           " current directory on computer where bot is installed \n" \
           "!Important - u cant use some CRUID commands like:" \
           " sudo, install. update, remove, purge etc. For security reason"
