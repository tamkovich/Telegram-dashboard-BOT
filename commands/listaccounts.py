import command_system


def listaccount(step, *args, **kwargs):
    message = "Not working right now ..."
    return (message, [], [], []), step


info_command = command_system.Command()

info_command.keys = ["/listaccounts"]
info_command.description = "List accounts/targets you have registered the bot (and are currently authenticated)."
info_command.process = listaccount
