from private.parse import parse_str

import command_system


def start(step, *args, **kwargs):
    message = parse_str('data_str', 'start.txt')
    return (message, [], [], []), step


info_command = command_system.Command()

info_command.keys = ["/start"]
info_command.description = "Starting action."
info_command.process = start
