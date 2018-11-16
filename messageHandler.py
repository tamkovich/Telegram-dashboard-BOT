import importlib
import os

from logic_application.telegramapi import Telegram
from command_system import command_list


def load_modules():
    files = os.listdir("commands")
    modules = filter(lambda x: x.endswith(".py"), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(step, action, content=None):
    message = "Sorry, I don't understand you. Write /help to know about my commands"
    for c in command_list:
        for k in c.keys:
            if action == k:
                return c.process(step, content) if content else c.process(step, action)
    return (message, "", [], []), step


def _action_detect(action, data_text):
    text = None
    if action.startswith('/'):
        action = action.split(' ')[0]
        text = data_text[len(action):].strip()
    return action, text


def create_answer(data, token, step):
    load_modules()
    tg = Telegram(token)
    user_id = data["chat"]["id"]
    action = data.get("text", '')

    # распознование команд
    action, text = _action_detect(action, action)

    args, step = get_answer(step, action, text)
    print(args)
    tg.send_message(user_id, args[0], args[1], args[2], args[3])
    return step
