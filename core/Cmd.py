import os
import subprocess
from core import config


class Cmd:
    # disallowed shell commands.
    disallowed_commands = [
        'remove',
        'install',
        'apt',
        'get',
        'update',
        'delete',
        'purge',
        'sudo',
    ]

    def run_shell(self, command):
        if not config.function_is_owner_exist():
            return "Only owner can run"

        cmd_command = self.get_command(command)
        if not self.is_command_allowed(cmd_command):
            return "Not all CRUID commands allowed. Read only operations."

        return 0

    def is_command_allowed(self, command):
        result = True
        for value in self.disallowed_commands:
            if value in command:
                result = False

        return result


    def get_command(self, command):
        return command.replace('/cmd', '')
