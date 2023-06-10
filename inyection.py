from kink import di
from os import getenv
from ebooklib import epub
from gpt.poe_api import PoeGPT
from gpt.epub_process.db.json_database import ImplementedJsonDB
from gpt.epub_process.db.vector_database import VectorStore


def config(epub_path:str = None, db_name:str = None):
    db_path, epub_path, gpt_token = boostrap(epub_path, db_name)

    #EpubProcessor used: ebooklib
    epub_ebook = epub.read_epub(epub_path)
    di['epub_ebook'] = epub_ebook

    #JsonDB used: pinkledb
    di['db'] = ImplementedJsonDB(db_name)

    #GPT used: Poe
    di['gpt'] = PoeGPT(gpt_token, 'a2', 30)

def boostrap(epub_path: str = None, db_name:str = None):
    db_path = getenv('EPUB_GPT_JSON_DB', db_name)
    epub_path = getenv('EPUB_GPT_PATH', epub_path)
    gpt_token = getenv('GPT_POE_KEY', "43PBP12f8kaplX0hkDxXFA%3D%3D")
    return db_path, epub_path, gpt_token