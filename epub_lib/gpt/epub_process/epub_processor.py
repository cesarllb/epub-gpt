import os
import ebooklib
from tqdm import tqdm
from kink import inject
from .db.repo import Repository
from .xhtml_processor import XHTMLProcessor


class Ebook_Lib:

    @inject
    def __init__(self, ebook_lib_loader: function) -> None:
        self._ebook_lib = ebook_lib_loader()

    def get_items_of_type(self, item_type:str):
        return self._ebook_lib.get_items_of_type(item_type)

class EpubProcessor:

    def __init__(self):
        self.repo = Repository()
        epub = Ebook_Lib()
        documents = epub.get_items_of_type(ebooklib.ITEM_DOCUMENT)
        for doc in tqdm(documents):
            content = doc.content.decode('utf-8')
            if content.startswith('<?xml') and 'xhtml' in content:
                xhtml = XHTMLProcessor(content)
                name = doc.get_name().split('/')[1].split('.')[0]
                self.repo.insert(name, xhtml.text.strip(), xhtml.p_list)


    
    

