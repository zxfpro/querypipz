""" cleaner 文本清洗"""
import re
from enum import Enum
from typing import Any
from promptlibz import Templates,TemplateType
from llama_index.core.schema import TransformComponent
from llmada import BianXieAdapter
from llama_index.core import Document
class DeDaoCleaner(TransformComponent):
    """专为得到设计的清理类

    Args:
        TransformComponent (_type_): _description_
    """
    def __call__(self, nodes, **kwargs):
        prompt = Templates(TemplateType.DedaoExtract)
        bx = BianXieAdapter()
        # bx = GoogleAdapter("AIzaSyBH4ut1plgB95fEiBlBXq1S-VrdYY5xPU4")
        for node in nodes:
            result = bx.product(prompt.format(text = node.text))
            node.set_content(self._extract_n_code(result))
        return nodes

    def _extract_n_code(self,text: str)->str:
        """从文本中提取python代码

        Args:
            text (str): 输入的文本。

        Returns:
            str: 提取出的python文本
        """
        pattern = r'```原文摘抄([\s\S]*?)```'
        matches = re.findall(pattern, text)
        return matches[0]
    
class ExtractConceptCleaner(TransformComponent):
    """专为得到设计的清理类

    Args:
        TransformComponent (_type_): _description_
    """
    def __call__(self, nodes, **kwargs):

        prompt = """
**优化的提示词模板：**

```memory
<Concept: <The name of the specific personal concept, e.g., 黄英杰>>

---
<Description: <A description of the concept, including identifying information like name, relationships, or roles.>>

---
<Event: <Specific events, interactions, or details related to the concept mentioned in the conversation. Include relevant locations if mentioned.>>
```

**优化思考：**

1.  **聚焦个人差异性概念：** 明确指示只提取“有别于常识的个人差异性概念”，这自然会将重点放在人物（及其独特的经历和关系）和特定地点上，排除普遍性概念。
2.  **信息汇集：** 模板通过 `<Concept>`, `<Description>`, 和 `<Event>` 三个部分，强制将关于同一概念的不同信息（名字、描述、相关事件）聚合在一起，满足了信息汇集的要求。
3.  **对话提取：** 提示词任务本身就是基于对话进行的提取，因此模板是为从对话中提取信息而设计的。
4.  **特定格式：** 模板严格遵循了要求的输出格式。
5.  **清晰的指令：** 在实际使用时，会进一步补充指令，明确说明提取范围（人物为主，地点辅之），以及对“有别于常识”的理解（例如，一个普通的朋友名字不是特异概念，但一个特定职业或经历的朋友就是）。

{chat_history}
"""
        bx = BianXieAdapter()
        memr2 = []
        for node in nodes:
            result = bx.product(prompt.format(chat_history = node.text))
            memorys = self._extract_n_memory(result)
            memr = []
            for memory in memorys:
                memr.append(Document(text = self._extract_concept(memory),metadata = {"docs":memory}))
            memr2.extend(memr)
            
        return memr2
    
    def _extract_concept(self,text: str)->str:
        """从文本中提取python代码

        Args:
            text (str): 输入的文本。

        Returns:
            str: 提取出的python文本
        """
        pattern = r'<Concept: ([\s\S]*?)>'
        matches = re.findall(pattern, text)
        return matches[0]

    def _extract_n_memory(self,text: str)->str:
        """从文本中提取python代码

        Args:
            text (str): 输入的文本。

        Returns:
            str: 提取出的python文本
        """
        pattern = r'```memory([\s\S]*?)```'
        matches = re.findall(pattern, text)
        return matches

class CleanerType(Enum):
    """types
    """
    DE_DAO_CLEANER = 'DeDaoCleaner'
    EXTRACT_CONCEPT_CLEARER = "ExtractConceptCleaner"
    # 添加更多选项

class Cleaner:
    """文本清洗
    """
    def __new__(cls, clean_type: CleanerType | str) -> Any:
        if isinstance(clean_type,CleanerType):
            assert clean_type.value in [i.value for i in CleanerType]
            key_name = clean_type.value
        else:
            assert clean_type in [i.value for i in CleanerType]
            key_name = clean_type
        instance = None

        if key_name == 'DeDaoCleaner':
            instance = DeDaoCleaner()

        elif key_name == 'ExtractConceptCleaner':
            instance = ExtractConceptCleaner()

        else:
            raise TypeError('Unknown type')

        return instance
