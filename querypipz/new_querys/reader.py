# Reader 工厂模式


from enum import Enum
from typing import List, Any

from enum import Enum
from typing import List, Any
from llama_index.core.readers.base import BaseReader
from typing import List, Dict,Optional
from llama_index.core import Document
import yaml
from .utils import get_data_from_md
    
class CustObsidianReader1(BaseReader):
    def load_data(self, file_path: str,
                        extra_info: Optional[Dict] = None) -> List[Document]:
        # 自定义读取逻辑
        with open(file_path, 'r') as file:
            text = file.read()
        data,content = get_data_from_md(text)
        # 使用状态
        status = data.get('编辑状态',None)
        topic = data.get('topic','')
        describe = data.get('describe','')
        creation_date = data.get("creation date",'')
        tags = data.get('tags', [])
        link = data.get('链接','')
        content_cut = content[:6000]
        if len(content_cut) != len(content):
            print(topic,'is too long ***')


        document = Document(text=f"topic: {topic} content: {content}", 
                            metadata={"topic":topic,
                                      "status":status,
                                      "creation_date":str(creation_date),
                                      "tags":tags,
                                      "link":link},
                           )
        return [document]


class ReaderType(Enum):
    Simple = 'CustObsidianReader1'
    Simple2 = 'Simple2'
    # 添加更多选项

class Reader:
    def __new__(cls, type: ReaderType) -> Any:
        assert type.value in [i.value for i in ReaderType]
        instance = None

        if type.value == 'CustObsidianReader1':
            instance = CustObsidianReader1()
            # instance = SomeClass(param1=value1, param2=value2)

        elif type.value == 'Simple2':

            # instance = AnotherClass(param1=value1, param2=value2)
            pass


        else:
            raise Exception('Unknown type')

        return instance



######################






# Spliter 工厂模式

from enum import Enum
from typing import List, Any

class SplitterType(Enum):
    Simple = 'Simple'
    Simple2 = 'Simple2'
    # 添加更多选项

class Splitter:
    def __new__(cls, type: SplitterType) -> Any:
        assert type.value in [i.value for i in SplitterType]
        instance = None

        if type.value == 'Simple':

            # instance = SomeClass(param1=value1, param2=value2)
            pass

        elif type.value == 'Simple2':

            # instance = AnotherClass(param1=value1, param2=value2)
            pass


        else:
            raise Exception('Unknown type')

        return instance

# Index 工厂模式  特异化自定义


from enum import Enum
from typing import List, Any

class IndexType(Enum):
    Simple = 'Simple'
    Simple2 = 'Simple2'
    # 添加更多选项

class Indexs:# 配合store 
    def __new__(cls, type: IndexType) -> Any:
        assert type.value in [i.value for i in IndexType]
        instance = None

        if type.value == 'Simple':

            # instance = SomeClass(param1=value1, param2=value2)
            pass

        elif type.value == 'Simple2':

            # instance = AnotherClass(param1=value1, param2=value2)
            pass


        else:
            raise Exception('Unknown type')

        return instance
    
from enum import Enum
from typing import List, Any

class RetriverType(Enum):
    Simple = 'Simple'
    Simple2 = 'Simple2'
    # 添加更多选项

class Retriver:
    def __new__(cls, type: RetriverType) -> Any:
        assert type.value in [i.value for i in RetriverType]
        instance = None

        if type.value == 'Simple':

            # instance = SomeClass(param1=value1, param2=value2)
            pass

        elif type.value == 'Simple2':

            # instance = AnotherClass(param1=value1, param2=value2)
            pass


        else:
            raise Exception('Unknown type')

        return instance
    

from enum import Enum
from typing import List, Any
from llama_index.core import SimpleDirectoryReader


class QueryType(Enum):
    Simple = 'Simple'
    Simple2 = 'Simple2'
    # 添加更多选项

class Query:
    def __new__(cls, type: QueryType) -> Any:
        assert type.value in [i.value for i in QueryType]
        instance = None

        if type.value == 'Simple':

            # instance = SomeClass(param1=value1, param2=value2)
            pass

        elif type.value == 'Simple2':

            # instance = AnotherClass(param1=value1, param2=value2)
            pass


        else:
            raise Exception('Unknown type')

        return instance


# 目的是将构建过程与表示分开

class Queryer:
    def __init__(self):
        self.reader = None
        self.splitter = None
        self.index = None
        self.retriver = None
        self.query = None

    def __str__(self):
        return f"House with self.foundation, self.structure, self.roof, and self.interior"

# 生成器接口
class QueryBuilder:
    def build_reader(self):
        pass

    def build_splitter(self):
        pass

    def build_index(self):
        pass

    def build_retriver(self):
        pass

    def build_query(self):
        pass

    def build_knowledge(self):
        pass

    def get_query(self):
        pass

# 具体生成器
class QueryBuilder1(QueryBuilder):
    # TODO 做一个模式
    def __init__(self):
        self.query = Queryer()
    
    def build_reader(self):
        file_path = 'work1'        
        self.query.reader = SimpleDirectoryReader(input_dir=file_path,
                                          file_extractor = {".pdf": Reader(ReaderType.Simple)},
                                          recursive=True,
                                          exclude=["*.mp3"],
                                          )

    def build_splitter(self):
        self.query.splitter = "splitter"

    def build_index(self):
        self.query.index = "index"

    def build_retriver(self):
        self.query.retriver = "retriver"

    def build_query(self):
        self.query.query = "query"

    def build_knowledge(self):
        self.query.build = "build"

    def get_query(self):
        return self.query
    
# 具体生成器
class QueryBuilder2(QueryBuilder):
    def __init__(self):
        self.query = Queryer()

    
    def build_reader(self):
        self.query.reader = "Reader"

    def build_splitter(self):
        self.query.splitter = "splitter"

    def build_index(self):
        self.query.index = "index"

    def build_retriver(self):
        self.query.retriver = "retriver"

    def build_query(self):
        self.query.query = None

    def build_knowledge(self):
        self.query.build = "build"

    def get_query(self):
        if self.query.query is None:
            return index.as_query_engine(similarity_top_k=similarity_top_k)


# 具体生成器
class QueryBuilder3(QueryBuilder):
    '''

# 定义提示模板字符串
template_str = """
Take a deep breath and work on this problem step-by-step

您是一个Python工程师, 我会提供给您一些已验证可用的代码(防止出现包版本过旧,或者环境不支持的情况),
在代码编写中,如果被验证代码块中存在相关内容,您应该尽可能的使用被验证的代码, 而非经验.
基于用户的需求和提供的已验证代码, 结合自己的经验,编写代码.
您编写的代码应该封装成函数或者类


已验证代码:
---
```python
{safe_code}
```
---

用户的诉求:
{prompt}

输出函数:
"""

# 创建PromptTemplate实例
qa_prompt = PromptTemplate(template=template_str)


class PythonQueryEngine(CustomQueryEngine):
    """RAG String Query Engine."""

    retriever: BaseRetriever
    response_synthesizer: BaseSynthesizer
    llm: OpenAI
    qa_prompt: PromptTemplate
    stream:bool

    def custom_query(self, query_str: str):
        # custom_query(query_str: str) -> STR_OR_RESPONSE_TYPE
        # acustom_query(query_str: str) -> STR_OR_RESPONSE_TYPE

        queries = query_str.split('&')
        nodes = []
        for query_str in queries:
            nodes += self.retriever.retrieve(query_str)
        # nodes = self.retriever.retrieve(query_str)
        print(query_str,'query_str')
        context_str = "\n\n".join([n.node.get_metadata_str() for n in nodes])
        if self.stream:
            response = self.llm.stream_complete(
                qa_prompt.format(safe_code=context_str, prompt=query_str)
            )

            def response_gen():
                i = [0]
                for r in response:
                    i.append(len(str(r)))
                    yield str(r)[i[-2]:]

            return StreamingResponse(response_gen=response_gen(),source_nodes=nodes)
        else:
            response = self.llm.complete(qa_prompt.format(safe_code=context_str, prompt=query_str))
    
            response_obj = self.response_synthesizer.synthesize(response.text, nodes)
            return Response(response=response.text,source_nodes=nodes) # TODO 增加metadata



    '''
    def __init__(self):
        self.query = Queryer()

    
    def build_reader(self):
        self.query.reader = "Reader"

    def build_splitter(self):
        self.query.splitter = "splitter"

    def build_index(self):
        self.query.index = "index"

    def build_retriver(self):
        self.query.retriver = None

    def build_query(self):
        self.query.query = "query"

    def build_knowledge(self):
        self.query.build = "build"

    def get_query(self):
        # 例如：
            # instance = AnotherClass(param1=value1, param2=value2)
        
        
        retriever = index.as_retriever(similarity_top_k=similarity_top_k)
        qurw =  query_engine = PythonQueryEngine(
                retriever=retriever,
                response_synthesizer=get_response_synthesizer(response_mode="compact"),
                llm=Settings.llm,
                qa_prompt=qa_prompt,
                stream = True,
            )

        return qurw





# 指挥者
class Director:
    def __init__(self, builder:QueryBuilder):
        self.builder = builder

    def construct(self):
        self.builder.build_reader()
        self.builder.build_splitter()
        self.builder.build_index()
        self.builder.build_retriver()
        self.builder.build_query()
        return self.builder.get_query()

if __name__ == "__main__":
    # 客户端代码
    builder = QueryBuilder1()
    director = Director(builder)
    query = director.construct()
    print(query)  

    # query pipeline

    # chat

    # workflow





##########


