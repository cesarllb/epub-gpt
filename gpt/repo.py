from kink import di, inject
from .interface import IGPTClient
from .gpt_functions import resume, explain_text, translate_text, define_word, describe_own_name


class GptRepo:

    @inject
    def __init__(self, gpt: IGPTClient) -> None:
        self._gpt = gpt
     
    def send_message(self, message:str) -> str:
        return self._gpt.send_message(message)
     
    def resume(self, topic:str) -> str:
        return resume(self._gpt, topic)

    def explain_text(self, text:str) -> str:
        return explain_text(self._gpt, text)
     
    def describe_own_name(self, noun:str) -> str:
        return describe_own_name(self._gpt, noun)
     
    def translate_text(self, text:str, language:str) -> str:
        return translate_text(self._gpt, text, language)
     
    def define_word(self, word:str) -> str:
        return define_word(self._gpt, word)

