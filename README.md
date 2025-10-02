# querypipz

我们的任务就是要构建一个在query 之前, 甚至在chat 之前的所有动作的包

#  应该如何使用该仓库
1 合理的维护所有的factory 工厂
    例如 docstore, vectorstore, graphstore

2 构建并存续特异化的builderlib

3 注册到director 中的 buildtype中

"""
    VectorStore        from document      from vectorstore
    内有数据             √(创建时会存储)              √(及时存储)
    内无数据                  √                     √(需要以创建)
"""

###

0-1 query pipeline
1 多模态
2 

