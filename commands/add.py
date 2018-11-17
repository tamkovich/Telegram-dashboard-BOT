import command_system

from logic_application import api_usage


def add(step, msg):
    step = 0
    try:
        username, password = msg.split(':')
    except ValueError:
        return ('Invalid message', [], [], []), step
    data = {
        'accountName': username,
        'description': username,
        'useProxy': 'true',
        'tag': '100k',
        'username': username,
        'password': password
    }
    if step == 0:
        message, step = api_usage.add_account(data)
        
    else:
        message = 'You have to finish your last step'
    return (message, [], [], []), step


info_command = command_system.Command()

info_command.keys = ["/add"]
info_command.description = "Add an account to the bot."
info_command.process = add
