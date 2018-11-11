import command_system


def hello(*args, **kwargs):
    message = "Hi, how are you!"
    return message, [], [], []


hello_command = command_system.Command()

hello_command.keys = ["hello", "hi"]
hello_command.description = "Greeting you!"
hello_command.process = hello
