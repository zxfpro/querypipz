from enum import Enum
from typing import Type

# 导入 ReaderStrategy
from .reader_strategies import (
    BaseReaderStrategy,
    CustObsidianReaderStrategy,
    # 导入你将来添加的 Strategy
)
from llama_index.core.readers.base import BaseReader

class ReaderType(Enum):
    OBSIDIAN = 'OBSIDIAN' # 更具描述性的名称
    DEFAULT = 'DEFAULT'    # 例如用于 SimpleDirectoryReader 的默认行为
    # 添加更多选项

class ReaderStrategyFactory:
    """Factory to create different reader strategy instances."""

    # 注册策略的字典
    _strategies: dict[ReaderType, Type[BaseReaderStrategy]] = {
        ReaderType.OBSIDIAN: CustObsidianReaderStrategy,
        # ReaderType.DEFAULT: DefaultReaderStrategy, # 如果有默认策略的话
        # 在这里注册你将来添加的策略
        # ReaderType.ANOTHER_TYPE: AnotherReaderStrategy,
    }

    @classmethod
    def get_strategy(cls, reader_type: ReaderType) -> BaseReaderStrategy:
        """Get the reader strategy instance based on the reader type."""
        strategy_cls = cls._strategies.get(reader_type)
        if strategy_cls is None:
            raise ValueError(f"Unknown reader type: {reader_type}")
        return strategy_cls()

class ReaderFactory:
    """Factory to create different reader instances using strategies."""

    @classmethod
    def create_reader(cls, reader_type: ReaderType) -> BaseReader:
        """Create and configure a reader instance based on type."""
        strategy = ReaderStrategyFactory.get_strategy(reader_type)
        reader = strategy.build_reader()
        return reader
