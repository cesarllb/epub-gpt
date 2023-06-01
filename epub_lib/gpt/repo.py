from kink import inject
from .interface import IGPTClient

class GptRepo:

    @inject
    def __init__(self, gpt: IGPTClient) -> None:
        self._gpt = gpt
     
    def send_message(self, message:str) -> str:
        return self._gpt.send_message(message)
     
    def resume(self, topic:str) -> str:
        return self._gpt.resume(topic)

    def explain_text(self, text:str) -> str:
        return self._gpt.explain_text(text)
     
    def describe_own_name(self, noun:str) -> str:
        return self._gpt.describe_own_name(noun)
     
    def translate_text(self, text:str, language:str) -> str:
        return self._gpt.translate_text(text, language)
     
    def define_word(self, word:str) -> str:
        return self._gpt.define_word(word)