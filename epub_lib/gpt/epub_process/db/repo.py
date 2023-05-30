from .database import ImplementedJsonDB

class Repository:

    def __init__(self, path:str = ''):
        self.__db = ImplementedJsonDB(path)

    def insert(self, xhtml_file_name:str, text: str, p_list:list):
        self.__db.insert(xhtml_file_name, text, p_list)

    def get_xhtml(self, index:int = None, xhtml_file_name:str = None) -> dict:
        return self.__db.get_xhtml(index, xhtml_file_name)

    def remove_xhtml(self, index:int = None, xhtml_file_name:str = None) -> bool:
        return self.__db.remove_xhtml( index= index, xhtml_file_name=xhtml_file_name)

    def search_str(self, str_to_find: str, num_words_around:int = None) -> str:
        return self.__db.search_str(str_to_find, num_words_around)

