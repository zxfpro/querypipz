from abc import ABC, abstractmethod
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.base.response.schema import Response, StreamingResponse
from llama_index.core.response_synthesizers import BaseSynthesizer
from llama_index.core.retrievers import BaseRetriever
from llama_index.core.query_engine import CustomQueryEngine
from llama_index.llms.openai import OpenAI
from llama_index.core import PromptTemplate
from typing import Optional, Any
from llama_index.core import (
    get_response_synthesizer,
    Settings,
)

# 导入你定义的 qa_prompt
from .querys import qa_prompt

class BaseQueryStrategy(ABC):
    """Abstract base class for different query strategies."""

    @abstractmethod
    def build_query_engine(self, index: VectorStoreIndex, **kwaargs) -> Any:
        """Build and return a specific query engine instance."""
        pass

class LlamaIndexDefaultQueryStrategy(BaseQueryStrategy):
    """Strategy for the default LlamaIndex query engine."""

    def build_query_engine(self, index: VectorStoreIndex, similarity_top_k: int = 3, **kwargs) -> Any:
        """Build and return the default LlamaIndex query engine."""
        return index.as_query_engine(similarity_top_k=similarity_top_k)

class PythonQueryEngineStrategy(BaseQueryStrategy):
    """Strategy for the Custom PythonQueryEngine."""

    def build_query_engine(self, index: VectorStoreIndex, similarity_top_k: int = 3, stream: bool = True, **kwargs) -> Any:
        """Build and return the Custom PythonQueryEngine."""
        retriever = index.as_retriever(similarity_top_k=similarity_top_k)
        response_synthesizer = get_response_synthesizer(response_mode="compact")

        # Assuming Settings.llm is already set
        llm = Settings.llm

        query_engine = PythonQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
            llm=llm,
            qa_prompt=qa_prompt,
            stream=stream,
        )
        return query_engine

# 你可以继续添加更多 QueryStrategy 的实现
# class AnotherQueryEngineStrategy(BaseQueryStrategy):
#     def build_query_engine(self, index: VectorStoreIndex, **kwargs) -> Any:
#         # Build and return another type of query engine
#         pass


# 保留你的 CustomQueryEngine，但将其移到这个文件中或者一个单独的实现文件中
class PythonQueryEngine(CustomQueryEngine):
    """RAG String Query Engine."""
    retriever: BaseRetriever
    response_synthesizer: BaseSynthesizer
    llm: OpenAI
    qa_prompt: PromptTemplate
    stream: bool

    # 将依赖通过构造函数注入
    def __init__(self, retriever: BaseRetriever, response_synthesizer: BaseSynthesizer, llm: OpenAI, qa_prompt: PromptTemplate, stream: bool):
        super().__init__(retriever=retriever, response_synthesizer=response_synthesizer, llm=llm, qa_prompt=qa_prompt, stream=stream)
        self.retriever = retriever
        self.response_synthesizer = response_synthesizer
        self.llm = llm
        self.qa_prompt = qa_prompt
        self.stream = stream

    def custom_query(self, query_str: str):
        queries = query_str.split('&')
        nodes = []
        for q in queries: # 使用更清晰的变量名
            nodes += self.retriever.retrieve(q)

        context_str = "\n\n".join([n.node.get_metadata_str() for n in nodes])

        if self.stream:
            response = self.llm.stream_complete(
                self.qa_prompt.format(safe_code=context_str, prompt=query_str) # 使用 self.qa_prompt
            )
            def response_gen():
                last_len = 0
                for r in response:
                     current_len = len(str(r))
                     yield str(r)[last_len:]
                     last_len = current_len

            return StreamingResponse(response_gen=response_gen(), source_nodes=nodes)
        else:
            response = self.llm.complete(self.qa_prompt.format(safe_code=context_str, prompt=query_str)) # 使用 self.qa_prompt
            response_obj = self.response_synthesizer.synthesize(response.text, nodes)
            # 保持与 streaming 一致的返回值类型，或者根据需要调整
            # LlamaIndex 的 query engine 通常返回 Response 或 StreamingResponse
            # 这里返回 Response 对象是一个好的选择
            return Response(response=response.text, source_nodes=nodes)
