from abc import ABC, abstractmethod



class IGPTClient(ABC):

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def send_message(self, message:str) -> str:
        ...

    @abstractmethod
    def resume(self, topic:str) -> str:
        ...

    @abstractmethod
    def explain_text(self, text:str) -> str:
        ...

    @abstractmethod
    def describe_own_name(self, noun:str) -> str:
        ...

    @abstractmethod
    def translate_text(self, text:str, language:str) -> str:
        ...

    @abstractmethod
    def define_word(self, word:str) -> str:
        ...