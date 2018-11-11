import command_system


def add(*args, **kwargs):
    message = "Not working right now ..."
    return message, [], [], []


info_command = command_system.Command()

info_command.keys = ["/add"]
info_command.description = "Add an account to the bot."
info_command.process = add
