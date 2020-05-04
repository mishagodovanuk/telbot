import subprocess


# class Cmd.
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

    # run shell.
    # string command
    # return string
    def run_shell(self, command):
        cmd_command = self.get_command(command)
        if not self.is_command_allowed(cmd_command):
            return "Not all CRUID commands allowed. Read only operations."

        shell = subprocess.run(
            cmd_command,
            shell=True,
            check=False,
            capture_output=True)
        return shell.stdout if shell.stdout else shell.stderr

    # is command allowed
    # string command
    # return bool
    def is_command_allowed(self, command):
        result = True
        for value in self.disallowed_commands:
            if value in command:
                result = False

        return result

    # get command
    # string command
    # return string
    def get_command(self, command):
        return command.replace('/cmd', '')
