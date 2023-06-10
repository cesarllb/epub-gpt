import chromadb
from .interface import IEpubTextDB

class VectorStore(IEpubTextDB):

    def __init__(self, path:str = ''):
        self.client = chromadb.Client()
        self.collections = []

    def insert(self, xhtml_file_name:str, p_list:list) -> bool:
        if len(p_list) > 0:
            coll = self.client.create_collection(name = xhtml_file_name)
            coll.add(documents = p_list, 
                    metadatas= [{"p_len": len(p)} for p in p_list],
                    ids= [str(i) for i in range(1, len(p_list)+1)])

            self.collections.append(coll)


    def get_xhtml(self, index:int = None, xhtml_file_name:str = None) -> dict:
        if index is not None and index < len(self.collections):
            return self.collections[index]
        elif xhtml_file_name is not None:
            return [self.client.get_collection(xhtml_file_name) for coll in self.client.list_collections() if coll.name == xhtml_file_name]

    def remove_xhtml(self, index:int = None, xhtml_file_name:str = None) -> bool:
        if index is not None and index < len(self.collections):
            self.client.delete_collection(name = self.collections[index].name)
            self.collections.pop(index)
            return True
        elif xhtml_file_name is not None:
            self.client.delete_collection(xhtml_file_name)
            self.collections.pop( [i for i, val in enumerate(self.collections) if val.name == xhtml_file_name ] )
            return True
        else:
            return False
        

    def search_str(self, str_to_find: str) -> str:
        list_of_ocurrences, list_of_distances = [], []
        for coll in self.client.list_collections():
            results = coll.query( query_texts = [ str_to_find ], include = ['documents', 'distances'])
            documents, distances = results['documents'][0], results['distances'][0]
            if len(documents) > 0:
                for doc, dist in zip(documents, distances):
                    list_of_ocurrences.append(doc)
                    list_of_distances.append(dist)

        index_of_higher_score = [ i for i, _ in sorted(enumerate(list_of_distances), key=lambda x: x[1], reverse=True)[0:3] ]
        
        return [ list_of_ocurrences[i] for i in index_of_higher_score ] 
