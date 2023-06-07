import ebooklib
from tqdm import tqdm
from kink import inject
from .db.repo import Repository
from .xhtml_processor import XHTMLProcessor


class Ebook_Lib:

    @inject
    def __init__(self, epub_ebook) -> None:
        print(type(epub_ebook))
        self._ebook_lib = epub_ebook

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
                try: 
                    name = doc.get_name().split('/')[1].split('.')[0]
                except IndexError as e:
                    name = doc.get_name()                    
                self.repo.insert(name, xhtml.p_list)
