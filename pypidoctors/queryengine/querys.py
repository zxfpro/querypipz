from llama_index.core import PromptTemplate
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
