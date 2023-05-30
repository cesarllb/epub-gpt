from bs4 import BeautifulSoup


class XHTMLProcessor:
    __soup: BeautifulSoup
    p_list: list = []
    text:str

    def __init__(self, xhtml:str):
        self.__soup = BeautifulSoup(xhtml, 'html.parser')

        for p in self.__soup.find_all('p'):
            if len(p.get_text()) > 10:
                self.p_list.append(p.get_text())
            
        self.text = self.__soup.get_text()

        


        