from enum import Enum
from typing import Any, Type

# 导入 QueryStrategy
from .query_strategies import (
    BaseQueryStrategy,
    LlamaIndexDefaultQueryStrategy,
    PythonQueryEngineStrategy,
    # 导入你将来添加的 Strategy
)
from llama_index.core import VectorStoreIndex

class QueryType(Enum):
    DEFAULT = 'DEFAULT'        # 更通用的名称
    PYTHON_ENGINE = 'PYTHON_ENGINE' # 更具描述性的名称
    # 添加更多选项，命名应该反映策略的功能

class QueryStrategyFactory:
    """Factory to create different query strategy instances."""

    # 注册策略的字典
    _strategies: dict[QueryType, Type[BaseQueryStrategy]] = {
        QueryType.DEFAULT: LlamaIndexDefaultQueryStrategy,
        QueryType.PYTHON_ENGINE: PythonQueryEngineStrategy,
        # 在这里注册你将来添加的策略
        # QueryType.ANOTHER_TYPE: AnotherQueryEngineStrategy,
    }

    @classmethod
    def get_strategy(cls, query_type: QueryType) -> BaseQueryStrategy:
        """Get the query strategy instance based on the query type."""
        strategy_cls = cls._strategies.get(query_type)
        if strategy_cls is None:
            raise ValueError(f"Unknown query type: {query_type}")
        return strategy_cls() # 返回策略的实例

class QueryEngineFactory:
    """Factory to create different query engine instances using strategies."""

    @classmethod
    def create_query_engine(
        cls,
        query_type: QueryType,
        index: VectorStoreIndex,
        **kwargs
    ) -> Any:
        """Create and configure a query engine instance based on type."""
        strategy = QueryStrategyFactory.get_strategy(query_type)
        query_engine = strategy.build_query_engine(index, **kwargs)
        return query_engine
