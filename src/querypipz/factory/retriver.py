""" retriver """
from enum import Enum
from typing import Any
from llama_index.core.objects import ObjectIndex
from llama_index.core import VectorStoreIndex

class RetriverType(Enum):
    """Retriver

    Args:
        Enum (_type_): _description_
    """
    TOOLS_RETRIVER = 'ToolsRetriver'
    # 添加更多选项


class Retriver:
    """_summary_
    """
    def __new__(cls, retriver_type: RetriverType | str,tools = None) -> Any:
        assert retriver_type.value in [i.value for i in RetriverType]


        assert retriver_type.value in [i.value for i in RetriverType]

        if isinstance(retriver_type,RetriverType):
            assert retriver_type.value in [i.value for i in RetriverType]
            key_name = retriver_type.value
        else:
            assert retriver_type in [i.value for i in RetriverType]
            key_name = retriver_type
        instance = None

        if key_name == 'ToolsRetriver':
            # if we were using an external vector store,
            #   we could pass the stroage context and any other kwargs
            # storage_context=storage_context,
            # embed_model=embed_model,
            # ...
            obj_index = ObjectIndex.from_objects(tools,index_cls=VectorStoreIndex)
            instance=obj_index.as_retriever(similarity_top_k=2)

        else:
            raise TypeError('Unknown type')
        return instance
