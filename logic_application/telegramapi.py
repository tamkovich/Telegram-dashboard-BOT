import telebot


class Telegram:

    FILE_URL = "https://api.telegram.org/file/bot{0}/{1}"

    def __init__(self, token=None):
        self.token = token
        self.api = telebot.TeleBot(token=token)

    @staticmethod
    def _keyboard(buttons: list):
        if buttons:
            markup = telebot.types.ReplyKeyboardMarkup(True, True)
            for button in buttons:
                markup.add(button)
            return markup
        return None

    def get_file_path(self, file_id):
        return self.api.get_file(file_id).file_path

    def get_file_url(self, file_id):
        return self.FILE_URL.format(self.token, self.get_file_path(file_id))

    def send_message(self, user_id, message, buttons: list, images: list, files: list):
        if not self.api.token:
            self.api.token = self.token
        self.api.send_chat_action(user_id, 'typing')
        self.api.send_message(user_id, message, reply_markup=self._keyboard(buttons), parse_mode='Markdown')
        for image in images:
            self._send_photo(user_id, None, image)
        for file in files:  # do something with files
            pass

    def _send_photo(self, user_id, message, file):
        message = message if message else None
        # self.api.send_chat_action(user_id, 'file load')
        with open(file, "rb") as photo:
            self.api.send_photo(user_id, photo, caption=message)
