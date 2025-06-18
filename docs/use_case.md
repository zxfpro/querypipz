
# 1 初始化 build
在第一次使用的时候,需要初始化, 
如果定义了reader 则text 是否传入均可
如果没有定义reader 则 比如传入text
```python
from querypipz import BuilderFactory,BuilderType,Director

dirs = Director(BuilderFactory(BuilderType.CHAT_HISTORY_MEMORY_BUILDER))

query = dirs.construct()



text = """
user: hello
assistant: Hello! How can I assist you today?
user: 你在说什么?
assistant: 你好！我可以帮你做些什么呢？
user: 考虑一下
assistant: 你能具体说明一下需要我考虑什么吗？
user: 考虑一下做一个皮卡丘
assistant: 你是想让我考虑做一个皮卡丘的什么呢？是画一个皮卡丘，还是制作一个皮卡丘模型，或者其他什么呢？请告诉我更多细节。
user: 让我想想
"""

query.build(text = text,cover= True)

```



# 2 初始化构建过以后, 直接update上传

```python
from querypipz import BuilderFactory,BuilderType,Director

dirs = Director(BuilderFactory(BuilderType.CHAT_HISTORY_MEMORY_BUILDER))

query = dirs.construct()



text = """
user: 再一次hello
assistant: Hello! How can I assist you today?
user: 你在说什么?
assistant: 你好！我可以帮你做些什么呢？
user: 考虑一下
assistant: 你能具体说明一下需要我考虑什么吗？
user: 考虑一下做一个皮卡丘
assistant: 你是想让我考虑做一个皮卡丘的什么呢？是画一个皮卡丘，还是制作一个皮卡丘模型，或者其他什么呢？请告诉我更多细节。
user: 让我想想
"""

query.update(prompt = text)
```

# 直接调取retriver 和query 不需要初始化

## retriver

```python
query.retrieve_search('hello')
```


## query

```python
query.query('hello')
```

## tools

```python
query.tools('kv.html')
```
