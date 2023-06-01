from bs4 import BeautifulSoup


class XHTMLProcessor:
    _soup: BeautifulSoup
    p_list: list = []
    text:str

    def __init__(self, xhtml:str):
        self._soup = BeautifulSoup(xhtml, 'html.parser')

        for p in self._soup.find_all('p'):
            if len(p.get_text()) > 10:
                self.p_list.append(p.get_text())
            
        self.text = self._soup.get_text()

        


        