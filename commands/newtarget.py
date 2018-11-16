import command_system


def newtarget(step, *args, **kwargs):
    message = "Not working right now ..."
    return (message, [], [], []), step


info_command = command_system.Command()

info_command.keys = ["/newtarget"]
info_command.description = "Change like target."
info_command.process = newtarget
