import poe
from selenium import webdriver
from .interface import IGPTClient
from .epub_process.epub_processor import EpubProcessor


class PoeGPT(IGPTClient):

    def __init__(self, TOKEN:str, model:str, timeout:int = 30):
        self.epub = EpubProcessor()
        self._client = poe.Client(TOKEN)
        self._model = model
        self._timeout = timeout

    def send_message(self, message: str) -> str:
        for chunk in self._client.send_message(self._model, message, timeout = self._timeout):
            pass
        return chunk["text"]        
    
    def _get_cookie_value(self):
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
    


# 
# 