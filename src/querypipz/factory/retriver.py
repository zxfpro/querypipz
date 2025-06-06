""" re"""
from enum import Enum
from typing import List, Any
from llama_index.core.objects import ObjectIndex
from llama_index.core import VectorStoreIndex

class RetriverType(Enum):
    """Retriver

    Args:
        Enum (_type_): _description_
    """
    ToolsRetriver = 'ToolsRetriver'
    Simple2 = 'Simple2'
    # 添加更多选项




class Retriver:
    """_summary_
    """
    def __new__(cls, retriver_type: RetriverType,tools = None) -> Any:
        assert retriver_type.value in [i.value for i in RetriverType]
        retriever = None
        if retriver_type.value == 'ToolsRetriver':
            # if we were using an external vector store, we could pass the stroage context and any other kwargs
            # storage_context=storage_context,
            # embed_model=embed_model,
            # ...
            obj_index = ObjectIndex.from_objects(tools,index_cls=VectorStoreIndex)
            retriever=obj_index.as_retriever(similarity_top_k=2)

        elif retriver_type.value == 'Simple2':
            pass
        else:
            raise TypeError('Unknown type')
        return retriever
