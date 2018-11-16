import command_system

from logic_application import api_usage


def verify(step, msg):
    data = {'code': msg}
    if step == 0:
        message = api_usage.verify(data)
        step = 1
    else:
        message = 'You have to finish your last step'
    return (message, [], [], []), step


info_command = command_system.Command()

info_command.keys = ["/verify"]
info_command.description = ""
info_command.process = verify
