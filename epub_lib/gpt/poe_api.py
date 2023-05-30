import poe
from selenium import webdriver
from epub_process.epub_processor import EpubProcessor
from gpt_client_interface import IGPTClient



class PoeGPT(IGPTClient):
    __client: object
    __POE_API_TOKEN:str
    __epub:EpubProcessor

    def __init__(self, epub_path:str):
        self.__epub = EpubProcessor(epub_path)
        self.__POE_API_TOKEN = "BdYAoutUrMrv3Y1q5dOjpg%3D%3D"
        self.__client = poe.Client(self.__POE_API_TOKEN)

    def send_message(self, message: str) -> str:
        for chunk in self.__client.send_message("chinchilla", message, timeout = 30):
            pass
        return chunk["text"]
    
    def __limit_num_words_to_context_windows_size(self, list_p:list) -> str:
        return_str = ''
        for p in list_p:
            return_str += '\n'
            for word in p.split(' '):
                if len(return_str.split(' ')) - 1 < 1000:
                    return_str += word + ' '
                else:
                    break
        return return_str

    
    def resume(self, topic:str) -> str:
        all_search_text = self.__epub.repo.search_str(str_to_find=topic)
        action = '--- Resume el texto anterior de manera clara en el idioma del texto'
        if all_search_text:
            resized_str = self.__limit_num_words_to_context_windows_size(all_search_text)
            return self.send_message(resized_str + action)
        else:
            return self.send_message(topic + action)
    
    def explain_text(self, text:str) -> str:
        all_search_text = self.__epub.repo.search_str(str_to_find=text)
        action = '--- Explica el texto anterior de manera clara en el idioma del texto'
        if all_search_text:
            resized_str = self.__limit_num_words_to_context_windows_size(all_search_text)
            return self.send_message(resized_str + action)
        else:
            return self.send_message(text + action)

    def describe_own_name(self, noun:str) -> str:
        if len(noun.split(' ')) > 4:
            raise Exception('El sustantivo propio debe tener menos de 4 palabras')
        
        all_search_text = self.__epub.repo.search_str(str_to_find=noun)
        if all_search_text:
            resized_str = self.__limit_num_words_to_context_windows_size(all_search_text)
            action = '--- Resume en una lista las caracteristicas de este sustantivo propio'
            return self.send_message(resized_str + action)

    def translate_text(self, text:str, language:str) -> str:
        action = f'--- Traduce el texto anterior solamente, en el idioma {language}. La salida es el texto traducido y nada más.'
        return self.send_message(text + action)

    def define_word(self, word:str) -> str:
        if len(word.split(' ')) == 1:
            action = '--- Define formalmente la palabra anterior'
            return self.send_message(word + action)
        else:
            return 'Lo sentimos, solo se puede definir una sola palabra'
    
    
    def __get_cookie_value(self):
        cookie_value = ''
        for browser in ['edge', 'firefox', 'chrome', 'safari']:
            try:
                driver = getattr(webdriver, browser.capitalize())()
                driver.get('https://www.poe.com/')
                cookie = driver.get_cookie('p-b')
                if cookie:
                    cookie_value = cookie['value']
                    driver.quit()
                    break
                driver.quit()
            except Exception as e:
                print(f'Error with {browser}: {e}')
                
        return cookie_value


poe_api_var = PoeGPT('/home/cesar-linares/Documentos/lite_project/test.epub')
print(poe_api_var.define_word('casa'))