import chromadb
from chromadb.config import Settings
from interface import IVectorStore


class VectorStore(IVectorStore):
    client:object
    collection:object

    def __init__(self, colection_name:str):
        self.client = chromadb.Client()
        self.collection = self._create_collection(colection_name)
        
    def _create_collection(self, colection_name:str):
        return self.client.get_or_create_collection(colection_name)

    def add(self, document:list, ids:list, metadata:list = None):
        if len(document) == len(ids):
            self.collection.add(
            documents=document, # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
            ids=ids, # unique for each doc
            )
        

    def get_similar_words(self, words:str, top_n=10):
        results = self.collection.query(query_texts=words, n_results=top_n,
        # where={"metadata_field": "is_equal_to_this"}, # optional filter
        # where_document={"$contains":"search_string"}  # optional filter
        )
        return results
    
    def get_synonym(self, word:str):
        threshold = 1.8
        result = vector.get_similar_words(word, top_n=1)
        distance = result['distances'][0][0]
        # return result['documents'][0][0] if distance > threshold else 'pepe'
        return result


    

# #Chroma Vector Store
# vector = VectorStore("test")
# doc = '''Los seudocelomados1​, (Pseudocoelomata), asquelmintos (Aschelminthes), nematelmintos (Nemathelminthes) o blastocelomados (Blastoceolomata, nombre propuesto por Brusca & Brusca)2​ son una agrupación de filos cuya cavidad general no es de origen mesodérmico y recibe el nombre seudoceloma (o seudocele) o blastoceloma. Antiguamente formaron un filo único, los asquelmintos (del griego askos, ampolla o saco y helmins gusanos, gusanos que tienen un tubo, el digestivo, dentro de otro, la pared corporal), pero las diversas clases que lo componían son hoy consideradas como filos independientes.'''
# vector.add(doc.split(' '), 
#             [str(i) for i in range(1, len(doc.split(' '))+1)])
# print(vector.get_synonym('identificador'))