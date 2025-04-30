import sys
import os
# 将项目根目录添加到 Python 路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from pypidoctors.build import build,ReaderType
from pypidoctors.query import Queryr,QueryType
from llama_index.core.base.response.schema import Response, StreamingResponse

# def test_build():
#     num_docs = build("/Users/zhaoxuefeng/GitHub/obsidian/工作/工程技术/学习", persist_dir="./my_kb", reader_type=ReaderType.OBSIDIAN, debug=True)
#     print(f"Total documents indexed: {num_docs}")

def test_query():
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