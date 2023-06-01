from .interface import IJsonDB
from kink import inject

class Repository:

    @inject
    def __init__(self, json_db:IJsonDB):
        self._db = json_db

    def insert(self, xhtml_file_name:str, text: str, p_list:list):
        self._db.insert(xhtml_file_name, text, p_list)

    def get_xhtml(self, index:int = None, xhtml_file_name:str = None) -> dict:
        return self._db.get_xhtml(index, xhtml_file_name)

    def remove_xhtml(self, index:int = None, xhtml_file_name:str = None) -> bool:
        return self._db.remove_xhtml( index= index, xhtml_file_name=xhtml_file_name)

    def search_str(self, str_to_find: str, num_words_around:int = None) -> str:
        return self._db.search_str(str_to_find, num_words_around)

