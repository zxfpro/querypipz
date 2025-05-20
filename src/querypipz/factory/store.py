



from enum import Enum
from typing import List, Any
from llama_index.core.vector_stores import SimpleVectorStore
from llama_index.vector_stores.faiss import FaissVectorStore
import faiss








class VectorStoreType(Enum):
    SimpleVectorStore = 'SimpleVectorStore'
    FAISS = 'FAISS'
    # 添加更多选项

class VectorStore:
    def __new__(cls, type: VectorStoreType) -> Any:
        assert type.value in [i.value for i in VectorStoreType]
        instance = None

        if type.value == 'SimpleVectorStore':
            instance = SimpleVectorStore()

        elif type.value == 'FAISS':
            # Create a FAISS index
            faiss_index = faiss.IndexFlatL2(1536)  # Example dimension
            instance = FaissVectorStore(faiss_index=faiss_index)
        else:
            raise Exception('Unknown type')

        return instance

