from telegram.ext import BaseFilter


class _FilterQuestion(BaseFilter):
    """
    Extends Telegram BaseFilter to create a filter that returns true if the
    message was a question.
    """

    def filter(self, message):
        return message.text.endswith('?')


filter_question = _FilterQuestion()
