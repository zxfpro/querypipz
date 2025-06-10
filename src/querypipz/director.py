''' 指挥者与建造者'''
from enum import Enum
from typing import Any

from .abc_ import QueryBuilder
from .builderlib import *
from .builderstablelib import *
# 指挥者
class Director:
    """指挥者
    """
    def __init__(self, builder:QueryBuilder):
        self.builder = builder

    def construct(self):
        """开始建造

        Returns:
            返回queryer: 建造成功的产品
        """
        self.builder.set_llm()
        self.builder.build_reader() # data loader
        self.builder.build_ingestion_pipeline()
        self.builder.build_kg_extractors() # extractor transformers
        self.builder.build_storage_context()
        self.builder.build_index()
        self.builder.build_retriver()
        self.builder.build_query_pipeline()
        self.builder.build_tools()

        return self.builder.get_queryer()

class BuilderType(Enum):
    """构造者清单

    Args:
        Enum (_type_): 选择构造者
    """
    OBSIDIAN_DATE_BUILDER = 'ObsidianDateBuilder'
    OBSIDIAN_HABIT_BUILDER = "ObsidianHabitBuilder"
    DEDAO_JYRK_BUILDER = "DeDaoJYRKBuilder"
    DEDAO_JYRK_BUILDER2 = "DeDaoJYRK2Builder"
    DEDAO_JYRK_BUILDER6 = "DeDaoJYRK6Builder"
    TEST_GRAPH_BUILDER = "TestGraphBuilder"
    TEST_GRAPH_BUILDER2 = "Test2GraphBuilder"
    TEST_GRAPH_BUILDER3 = "Test3GraphBuilder"
    HISTORY_MEMORY_BUILDER = "HistoryMemoryBuilder"
    HISTORY_MEMORY_BUILDER2 = "HistoryMemory2Builder"
    SIMPLE = 'simple'
    # 添加更多选项

class BuilderFactory:
    """构造者工厂

    Raises:
        ValueError: _description_

    Returns:
        builder: 构造者
    """
    _builders = {
        BuilderType.OBSIDIAN_DATE_BUILDER: ObsidianDateBuilder,
        BuilderType.OBSIDIAN_HABIT_BUILDER: ObsidianHabitBuilder,
        BuilderType.DEDAO_JYRK_BUILDER: DeDaoJYRKBuilder,
        BuilderType.DEDAO_JYRK_BUILDER2: DeDaoJYRK2Builder,
        BuilderType.DEDAO_JYRK_BUILDER6: DeDaoJYRK6Builder,
        BuilderType.TEST_GRAPH_BUILDER: TestGraphBuilder,
        BuilderType.TEST_GRAPH_BUILDER2: Test2GraphBuilder,
        BuilderType.TEST_GRAPH_BUILDER3: Test3GraphBuilder,
        BuilderType.HISTORY_MEMORY_BUILDER: HistoryMemoryBuilder,
        BuilderType.HISTORY_MEMORY_BUILDER2: HistoryMemory2Builder,
    }

    def __new__(cls, builder_type: BuilderType,persist_path=None) -> Any:
        if builder_type not in cls._builders:
            raise ValueError(f"Unknown builder type: {builder_type}")
        builder_class = cls._builders[builder_type]
        if persist_path:
            instance = builder_class(persist_path = persist_path)
        else:
            instance = builder_class()
        return instance
