from llama_index.core import load_index_from_storage, StorageContext
from .utils import get_llm

class Queryr():
    def __init__(self,persist_dir:str):
        get_llm()
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
        self.index = index
        self.query = None

    def load_query(self,similarity_top_k:int=3):
        self.query = self.index.as_query_engine(similarity_top_k = similarity_top_k)

    def query(self,prompt:str):
        '''
        '''
        return self.query(prompt)