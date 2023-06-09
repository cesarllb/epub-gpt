from abc import ABC, abstractmethod

class IEpubTextDB(ABC):
    db:object

    @abstractmethod
    def __init__(self, path:str = ''):
        ...

    @abstractmethod
    def insert(self, xhtml_file_name:str, p_list:list):
        ...

    @abstractmethod
    def get_xhtml(self, index:int = None, xhtml_file_name:str = None) -> dict:
        ...

    @abstractmethod
    def remove_xhtml(self, index:int = None, xhtml_file_name:str = None) -> bool:
        ...

    @abstractmethod
    def search_str(self, str_to_find: str) -> str:
        ...
    