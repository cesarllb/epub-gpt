import heapq
import string
import pickledb
from .interface import IJsonDB
from pydantic import BaseModel


class XhtmlJsonElement(BaseModel):
    xhtml_file_name:str
    text:str
    p_list:list


class ImplementedJsonDB(IJsonDB):
    _db:pickledb
    _xhtml_index:int

    def __init__(self, db_name:str):
        self._db = pickledb.load(db_name+'.db', False)
        self._xhtml_index = 0


    def insert(self, xhtml_file_name:str, text: str, p_list:list) -> None:
        xhtml = XhtmlJsonElement(xhtml_file_name = xhtml_file_name, text = text, p_list = p_list)
        self._db.set(str(self._xhtml_index), xhtml.dict())
        self._db.dump()
        self._xhtml_index += 1
    
    def get_xhtml(self, index:int = None, xhtml_file_name:str = None) -> dict:
        if not index and not xhtml_file_name:
            raise Exception("Both argument(index and xhtml_file_name) can't be None")
        elif index:
            return self._db.get(str(index))
        elif xhtml_file_name:
            count = 0
            for dict in self._db.get(str(count)):
                if dict['xhtml_file_name'] == xhtml_file_name:
                    return dict
                count+=1
    
    def remove_xhtml(self, index:str = None, xhtml_file_name:str = None) -> bool:
        if index is None and not xhtml_file_name:
            raise Exception("Both argument(index and xhtml_file_name) can't be None")
        elif index:
            self._db.rem(str(index))
            self._db.dump()
            return True
        elif xhtml_file_name:
            count = 0
            while(self._db.get(str(count))):
                if self._db.get(str(count))['xhtml_file_name'] == xhtml_file_name:
                    self._db.rem(str(count))
                    self._db.dump()
                    return True
                count+=1
        else:
            return False


    def search_str(self, str_to_find: str, num_words_around:int = None) -> list:
    
        def find_sublist(str_to_find_list_words:str, text_list_words:str):
            #Remove punctuation signs
            translator = str.maketrans('', '', string.punctuation)
            text_list_words_without_punctuation = [s.translate(translator) for s in text_list_words]
        
            n = len(str_to_find_list_words)
            for i in range(len(text_list_words_without_punctuation) - n + 1):
                if text_list_words_without_punctuation[i:i+n] == str_to_find_list_words:
                    return i
            return -1
        
        #If num_words_around is None, get the paragraph where the str_to_find is present
        count = 0
        list_of_ocurrences = []
        if not num_words_around:
            while(self._db.get(str(count))):
                for p in self._db.get(str(count))['p_list']:
                    if str_to_find in p:
                        list_of_ocurrences.append(p)
                count+=1
            return heapq.nlargest(3, list_of_ocurrences, key=len)
        elif num_words_around:
            while(self._db.get(str(count))):
                text = self._db.get(str(count))['text']
                text_list_words = text.split()
                str_to_find_list_words = str_to_find.split()
                pos_str_to_find_in_text= find_sublist(str_to_find_list_words, text_list_words)
                if pos_str_to_find_in_text != -1:
                    #return all the words in the text between the position where str_to_find are and the position of the last word of str_to_find plus num_words_around
                    list_of_ocurrences.append(' '.join(text_list_words[pos_str_to_find_in_text : pos_str_to_find_in_text + len(str_to_find_list_words) + num_words_around]))
                count+=1
            return heapq.nlargest(4, list_of_ocurrences, key=len)

        return "Not found"
    

