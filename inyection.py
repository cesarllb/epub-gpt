from kink import di
from os import getenv
from ebooklib import epub
from epub_lib.gpt.epub_process.db.database import ImplementedJsonDB
from epub_lib.gpt.poe_api import PoeGPT

def config():
    db_path, epub_path, gpt_token = boostrap()
    #JsonDB used: pinkledb
    di['json_db'] = ImplementedJsonDB(db_path)
    #EpubProcessor used: ebooklib
    di['ebook_lib_loader'] = lambda _ : epub.read_epub(epub_path)
    #GPT used: Poe
    di['gpt'] = PoeGPT(gpt_token, 'chinchilla', 30)

def boostrap():
    db_path = getenv('EPUB_GPT_JSON_DB', '')
    epub_path = getenv('EPUB_GPT_PATH', '/home/cesar-linares/Documentos/lite_project/test.epub')
    gpt_token = getenv('GPT_POE_KEY', "BdYAoutUrMrv3Y1q5dOjpg%3D%3D")
    return db_path, epub_path, gpt_token