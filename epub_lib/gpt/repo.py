from kink import di, inject
from .interface import IGPTClient
from .gpt_functions import resume, explain_text, translate_text, define_word, describe_own_name

class GptRepo:

    @inject
    def __init__(self, gpt: IGPTClient) -> None:
        self._gpt = gpt
     
    def send_message(self, message:str) -> str:
        return self._gpt.send_message(message)
     
    def resume(self, topic:str) -> str:
        return resume(self._gpt, topic)

    def explain_text(self, text:str) -> str:
        return explain_text(self._gpt, text)
     
    def describe_own_name(self, noun:str) -> str:
        return describe_own_name(self._gpt, noun)
     
    def translate_text(self, text:str, language:str) -> str:
        return translate_text(self._gpt, text, language)
     
    def define_word(self, word:str) -> str:
        return define_word(self._gpt, word)
    

# from ebooklib import epub
# from poe_api import PoeGPT
# from epub_process.db.database import ImplementedJsonDB

#     #EpubProcessor used: ebooklib
# epub_ebook = epub.read_epub('/media/cesar-linares/08050A6608050A66/Libros/prueba ahi/test.epub')
# di['epub_ebook'] = epub_ebook

# #JsonDB used: pinkledb
# di['json_db'] = ImplementedJsonDB('db_path')

# #GPT used: Poe
# di['gpt'] = PoeGPT('43PBP12f8kaplX0hkDxXFA%3D%3D', 'chinchilla', 30)

# poe_api_var = GptRepo()
# print(poe_api_var.describe_own_name('Charles Darwin'))