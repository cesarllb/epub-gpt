import os
import ebooklib
from ebooklib import epub
from .db.repo import Repository
from tqdm import tqdm
from .xhtml_processor import XHTMLProcessor

class EpubProcessor:
    repo: Repository

    def __init__(self, epub_path:str):
        db_name = os.path.basename(epub_path)
        self.repo = Repository(db_name)

        if not os.path.exists(db_name + '.db'):
            book = epub.read_epub(epub_path)
            documents = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)

            for doc in tqdm(documents):
                content = doc.content.decode('utf-8')
                if content.startswith('<?xml') and 'xhtml' in content:
                    xhtml = XHTMLProcessor(content)
                    name = doc.get_name().split('/')[1].split('.')[0]
                    self.repo.insert(name, xhtml.text.strip(), xhtml.p_list)


    
    

