from .interface import IVectorStore
import chromadb
from chromadb.config import Settings


class VectorStore(IVectorStore):
    client:object
    collection:object

    def __init__(self, colection_name:str):
        self.client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet"))
        self.collection = self.__create_collection(colection_name)
        
    def __create_collection(self, colection_name:str):
        return self.client.get_or_create_collection(colection_name)

    def add(self, document:list, metadata:dict, ids:list):
        if len(document) == len(metadata.keys()) == len(ids):
            self.collection.add(document, metadata, ids)
    
    
