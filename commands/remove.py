import command_system


def remove(*args, **kwargs):
    message = "Not working right now ..."
    return message, [], [], []


info_command = command_system.Command()

info_command.keys = ["/remove"]
info_command.description = "Remove an account."
info_command.process = remove
