import os
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, StorageContext
import shutil
# 导入新的 ReaderFactory 和 ReaderType
from .reader.reader_factory import ReaderFactory, ReaderType
from .utils import get_llm

def build(
    file_path: str,
    persist_dir="./obsidian_kb",
    reader_type: ReaderType = ReaderType.OBSIDIAN, # 使用新的 ReaderType
    debug: bool = True,
):
    # 确保 LLM 设置已加载
    get_llm()

    # 使用 ReaderFactory 创建 Reader 实例
    custom_reader = ReaderFactory.create_reader(reader_type)

    # LlamaIndex SimpleDirectoryReader 使用 file_extractor 来指定特定文件类型的 Reader
    file_extractor = {".md": custom_reader}

    reader = SimpleDirectoryReader(
        input_dir=file_path,
        file_extractor=file_extractor,
        recursive=True,
        # 加入 exclude 参数以排除不需要处理的文件或文件夹，例如 Obsidian 的 .obsidian 文件夹
        exclude=['.obsidian/*', '*.excalidraw.md'],
    )

    documents = reader.load_data()

    if debug:
        # 考虑使用更灵活的 debug 模式，例如只处理特定文件或目录
        print(f"Debug mode: Processing first 10 documents out of {len(documents)}")
        documents = documents[:10]

    if not documents:
        print("No documents loaded. Skipping index creation.")
        return 0

    print(f"Building index with {len(documents)} documents...")

    # 如果路径存在,则删除，或者考虑增量更新
    if os.path.exists(persist_dir):
        print(f"Deleting existing index storage at {persist_dir}")
        shutil.rmtree(persist_dir)

    # 确保 persist_dir 存在
    os.makedirs(persist_dir, exist_ok=True)

    index = VectorStoreIndex.from_documents(documents)

    # 持久化索引
    index.storage_context.persist(persist_dir=persist_dir)
    print(f"Index successfully built and saved to {persist_dir}")

    return len(documents)

# 示例用法 (如果需要在脚本中直接运行)
# if __name__ == "__main__":
#     # 假设你的 markdown 文件在 "./docs" 目录下
#     num_docs = build("./docs", persist_dir="./my_kb", reader_type=ReaderType.OBSIDIAN, debug=True)
#     print(f"Total documents indexed: {num_docs}")