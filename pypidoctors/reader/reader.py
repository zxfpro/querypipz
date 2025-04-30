# reader.reader.py
# 这个文件主要用来存放共享的 helper functions
import yaml
from typing import Dict, List, Optional
from llama_index.core import Document

def get_data_from_md(text):
    """Helper function to parse metadata and content from markdown with frontmatter."""
    # 确保 text 格式正确
    if text.strip().startswith("---"):
        parts = text.split("---", 2)
        if len(parts) < 3:
            raise ValueError("Markdown does not contain expected frontmatter format.")
        infos = parts[1]
        content = parts[2]
        data = yaml.safe_load(infos) if infos.strip() else {} # 即使 infos 为空也可以尝试加载
        return data if data is not None else {}, content
    else:
        # 如果没有 frontmatter，整个内容就是 content，metadata 为空
        return {}, text

# 可以保留原始的 CustObsidianReader 定义，但最好移到 reader_strategies.py 文件
# 或者只在这里保留 helper functions
# from llama_index.core.readers.base import BaseReader
# class CustObsidianReader(BaseReader):
#     # ... (moved to reader_strategies.py)
#     pass