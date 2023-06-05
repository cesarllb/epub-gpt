from abc import ABC, abstractmethod



class IGPTClient(ABC):

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def send_message(self, message:str) -> str:
        ...