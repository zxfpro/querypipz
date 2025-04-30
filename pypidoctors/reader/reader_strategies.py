from abc import ABC, abstractmethod
from llama_index.core.readers.base import BaseReader
from typing import Type, List, Dict, Optional
from llama_index.core import Document
import yaml

# 导入你的 get_data_from_md 函数
from .reader import get_data_from_md

class BaseReaderStrategy(ABC):
    """Abstract base class for different reader strategies."""

    @abstractmethod
    def build_reader(self) -> BaseReader:
        """Build and return a specific reader instance."""
        pass

class CustObsidianReaderStrategy(BaseReaderStrategy):
    """Strategy for the Custom ObsidianReader."""
    def build_reader(self) -> BaseReader:
        """Build and return the CustObsidianReader."""
        return CustObsidianReader()

# 添加更多 ReaderStrategy 的实现
# class AnotherReaderStrategy(BaseReaderStrategy):
#     def build_reader(self) -> BaseReader:
#         # Build and return another type of reader
#         pass


# 保留你的 CustObsidianReader，可以继续放在这个文件或单独实现文件
class CustObsidianReader(BaseReader):
    """Custom Reader for Obsidian Markdown files."""
    def load_data(self, file_path: str,
                        extra_info: Optional[Dict] = None) -> List[Document]:
        # 自定义读取逻辑
        with open(file_path, 'r', encoding='utf-8') as file: # 建议指定编码
            text = file.read()

        try:
            data, content = get_data_from_md(text)
        except Exception as e:
             print(f"Error parsing metadata from {file_path}: {e}")
             data = {}
             content = text # 如果解析失败，将整个文件内容作为 content

        # 使用状态
        status = data.get('编辑状态', None)
        topic = data.get('topic', '')
        describe = data.get('describe', '')
        creation_date = data.get("creation date", '')
        tags = data.get('tags', [])
        link = data.get('链接', '')
        # 确保 tags 是一个列表
        if isinstance(tags, str):
             tags = [tag.strip() for tag in tags.split(',')]
        # 清理 metadata 中的 None 值，或者根据需要处理
        metadata = {
            "topic": topic,
            "status": status,
            "creation_date": str(creation_date),
            "tags": tags,
            "link": link
        }
        # 过滤掉值为 None 的 metadata
        metadata = {k: v for k, v in metadata.items() if v is not None}


        # 根据你的需求决定如何处理过长的 content
        # content_for_embedding = content[:6000] # 例如用于 embedding 的部分
        # full_content = content # 保留完整的 content
        # LlamaIndex 的 Document 默认是将 text 用于 embedding， metadata 用于信息展示
        # 如果你希望将部分内容放入 metadata 或进行特殊处理，可以在这里调整

        # 确保 content 至少不为空
        if not content:
             content = "No content found."

        document = Document(text=f"topic: {topic} content: {content}", # 考虑如何格式化 text 更适合检索
                            metadata=metadata,
                           )
        return [document]