import command_system


def droptype(step, *args, **kwargs):
    message = "Not working right now ..."
    return (message, [], [], []), step


info_command = command_system.Command()

info_command.keys = ["/droptype"]
info_command.description = "Change account drop type."
info_command.process = droptype
