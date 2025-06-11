''' 指挥者与建造者'''

from querypipz.abc_ import QueryBuilder

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
