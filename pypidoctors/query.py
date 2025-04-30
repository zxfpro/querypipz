import os
from llama_index.core import load_index_from_storage, StorageContext
# 导入新的 QueryEngineFactory 和 QueryType
from .queryengine.query_factory import QueryEngineFactory, QueryType
from .utils import get_llm
from typing import Any

class Queryr:
    def __init__(self, persist_dir: str):
        # 确保 LLM 设置已加载
        get_llm()

        self.persist_dir = persist_dir
        self.index = None
        self.query_engine = None # 使用更通用的名称

        self._load_index()

    def _load_index(self):
        """Helper method to load the index from storage."""
        if not os.path.exists(self.persist_dir):
            raise FileNotFoundError(f"Index storage not found at {self.persist_dir}")
        print(f"Loading index from storage context at {self.persist_dir}")
        storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
        self.index = load_index_from_storage(storage_context)
        print("Index loaded successfully.")

    def set_query_engine(self, query_type: QueryType = QueryType.DEFAULT, **kwargs):
        """Set the query engine type and its specific parameters."""
        if self.index is None:
             raise RuntimeError("Index is not loaded. Cannot set query engine.")

        # 使用 QueryEngineFactory 创建 QueryEngine 实例
        self.query_engine = QueryEngineFactory.create_query_engine(
            query_type=query_type,
            index=self.index,
            **kwargs # 传递创建 QueryEngine 所需的参数，例如 similarity_top_k, stream 等
        )
        print(f"Query engine set to type: {query_type.value}")


    def ask(self, prompt: str) -> Any: # 返回类型根据 QueryEngine 的实际输出调整
        """Ask the query engine and return the response."""
        if self.query_engine is None:
            raise RuntimeError("Query engine is not set. Call set_query_engine first.")

        print(f"Asking with prompt: {prompt}")
        # QueryEngine.query() 方法返回 Response 或 StreamingResponse
        return self.query_engine.query(prompt)

# 示例用法 (如果需要在脚本中直接运行)
if __name__ == "__main__":
    # 假设你已经通过 build.py 构建了索引到 "./my_kb"
    persist_directory = "./my_kb"

    try:
        qr = Queryr(persist_dir=persist_directory)

        # 设置默认的 query engine
        qr.set_query_engine(query_type=QueryType.DEFAULT, similarity_top_k=5)

        # 提问
        response = qr.ask("告诉我关于PythonQueryEngine的说明")
        print("Response 1 (Default Engine):")
        print(response)

        # 切换到 PythonQueryEngine 并设置流式输出
        qr.set_query_engine(query_type=QueryType.PYTHON_ENGINE, similarity_top_k=3, stream=True)

        # 提问
        print("\nResponse 2 (PythonQueryEngine, streaming):")
        response_stream = qr.ask("编写一个简单的Python函数来计算斐波那契数列")

        # 处理流式响应
        if isinstance(response_stream, StreamingResponse):
             for text_chunk in response_stream.response_gen:
                 print(text_chunk, end="")
             print() # 打印换行

        # 注意 stream=False 时的 response 是 Response 对象
        # qr.set_query_engine(query_type=QueryType.PYTHON_ENGINE, similarity_top_k=3, stream=False)
        # response_non_stream = qr.ask("描述一下 CustObsidianReader 的功能")
        # print("\nResponse 3 (PythonQueryEngine, non-streaming):")
        # print(response_non_stream.response)


    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please run build.py first to create the index.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")