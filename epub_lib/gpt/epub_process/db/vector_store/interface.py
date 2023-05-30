from abc import ABC, abstractmethod

class IVectorStore(ABC):


    @abstractmethod
    def  __init__(self, colection_name:str):
        ...

    @abstractmethod
    def  get_vector(self, word):
        ...

    @abstractmethod
    def add(document:list, metadata:dict, ids:list):
        ...

    @abstractmethod
    def create_collection(self, colection_name:str):
        ...

    @abstractmethod
    def get_similar_words(self, word, top_n=10):
        ...

    @abstractmethod
    def get_similar_vectors(self, vector, top_n=10):
        ...
