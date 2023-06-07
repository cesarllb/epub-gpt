import os
import heapq
import pickledb
from .interface import IJsonDB
from pydantic import BaseModel

class XhtmlJsonElement(BaseModel):
    xhtml_file_name:str
    p_list:list

class ImplementedJsonDB(IJsonDB):
    _db:pickledb
    _xhtml_index:int

    def __init__(self, db_name:str):            
        if os.path.exists(db_name+'.db'):
            self._db = pickledb.load(db_name+'.db', auto_dump=False, sig= False)
        else:
            self._db = pickledb.load(db_name+'.db', auto_dump=False, sig= False)
        self._xhtml_index = 0


    def insert(self, xhtml_file_name:str, p_list:list) -> None:
        if len(p_list) > 0:
            xhtml = XhtmlJsonElement(xhtml_file_name = xhtml_file_name, p_list = p_list)
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


    def search_str(self, str_to_find: str) -> list:
        count = 0
        list_of_ocurrences = []
        while(self._db.get(str(count))):
            for p in self._db.get(str(count))['p_list']:
                if str_to_find in p:
                    list_of_ocurrences.append(p)
            count+=1
        return heapq.nlargest(3, list_of_ocurrences, key=len)
