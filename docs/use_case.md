```python
%cd ~/GitHub/querypipz/src/
```

    /Users/zhaoxuefeng/GitHub/querypipz/src



```python
from querypipz.director import BuilderFactory,BuilderType,Director
```


```python
director = Director(BuilderFactory(Builder.ObsidianHabitBuilder))
```


```python
query = director.construct()
```

## build


```python
query.build() #会覆盖我的记忆的  增加一个delete
```

    /Users/zhaoxuefeng/GitHub/obsidian/知识库/habit self.persist_path





    'builded'



## retriver


```python
query.retrieve('hello')
```




    [NodeWithScore(node=TextNode(id_='8bf46b2a-1271-4f73-ab62-58b990d7f4e1', embedding=None, metadata={'topic': '编码习惯', 'status': None, 'creation_date': '2025-05-19 18:34:26', 'tags': ['python'], 'link': ''}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node_id='8c95f708-5a45-4418-892c-eb1aa6062aaf', node_type='4', metadata={'topic': '编码习惯', 'status': None, 'creation_date': '2025-05-19 18:34:26', 'tags': ['python'], 'link': ''}, hash='6e573cf8e74cb3712e52a2b82c24e48744fec260b27d12626f8fe283329ada67'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node_id='eaf39ddb-857d-47ac-977a-f71052a1a55e', node_type='1', metadata={'topic': '编码习惯', 'status': None, 'creation_date': '2025-05-19 18:34:26', 'tags': ['python'], 'link': ''}, hash='e884add6791ef581a821ffeb488a38c9fae517d609b2342cc3b75cc4d4c17ecc')}, metadata_template='{key}: {value}', metadata_separator='\n', text='*   再进行工程化开发\n*   **熟悉的设计模式:** 工厂模式、单例模式、适配器模式、迭代器和生成器。\n*   **常用工具使用习惯:** 熟练使用 `code_interpreter` 进行代码验证、探索和调试，遵循其使用规范（使用 XML 标签、避免 Markdown 代码块、注重明确输出、提供分析和解释）。\n\n这份记录涵盖了你在编程语言、开发环境、代码管理、学习方式、代码风格、调试、测试、重构、工作流程、熟悉的设计模式以及常用工具使用等方面的习惯。\n\n**这份记录的意义在于：**\n\n*   **自我认知:** 帮助你更清晰地认识自己的编程偏好和工作方式。\n*   **优化提升:** 通过审视这些习惯，你可以发现可以改进或优化的方面。例如，如何更有效地与大模型交流，如何更好地组织 `print` 调试信息，或者如何进一步利用 `code_interpreter` 的功能。\n*   **沟通交流:** 如果你需要向他人描述你的编程习惯或偏好，这份记录可以提供一个很好的框架。\n\n你觉得这份记录是否准确地反映了你的编程习惯？还有没有其他你觉得重要的方面需要补充？我们可以根据需要随时调整和修改。', mimetype='text/plain', start_char_idx=1170, end_char_idx=1676, metadata_seperator='\n', text_template='{metadata_str}\n\n{content}'), score=0.7260945737960259),
     NodeWithScore(node=TextNode(id_='eaf39ddb-857d-47ac-977a-f71052a1a55e', embedding=None, metadata={'topic': '编码习惯', 'status': None, 'creation_date': '2025-05-19 18:34:26', 'tags': ['python'], 'link': ''}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node_id='8c95f708-5a45-4418-892c-eb1aa6062aaf', node_type='4', metadata={'topic': '编码习惯', 'status': None, 'creation_date': '2025-05-19 18:34:26', 'tags': ['python'], 'link': ''}, hash='6e573cf8e74cb3712e52a2b82c24e48744fec260b27d12626f8fe283329ada67'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node_id='8bf46b2a-1271-4f73-ab62-58b990d7f4e1', node_type='1', metadata={}, hash='d642fe98521bc1014a37c8ff584bc72f227480730e7129cb15e60232d645b715')}, metadata_template='{key}: {value}', metadata_separator='\n', text='topic: 编码习惯 content: \n\n好的，非常感谢你提供了这份关于 `code_interpreter` 工具的详细描述和使用规范。这让我们对你的习惯有了更深入的了解，特别是你如何利用这种交互式编程环境进行工作。\n\n根据你目前提供的所有信息，我可以为你总结一份更全面的个人编程习惯记录：\n\n**个人编程习惯记录**\n\n*   **主要编程语言:** Python\n*   **编程场景:** 主要围绕工作和个人学习\n*   **偏爱使用的 IDE/编辑器:**\n    *   Cursor (更适合工程化)\n    *   Jupyter Lab (更适合想法和调试)\n*   **代码管理方式:**\n    *   使用 Git + GitHub\n    *   自定义脚本辅助开始和编写 (脚本使用尚处于初级阶段，主要用于替代重复性工作)\n*   **学习和解决问题的方式:**\n    *   查阅开发文档\n    *   查阅对应网站\n    *   与大模型交流 (主要通过直接提问，有时因缺乏上下文而影响效果；协助完成代码生成、代码解释、网络服务、正则表达式等任务)\n    *   使用 `code_interpreter` 工具进行交互式编程和调试 (用于快速执行代码进行分析、计算或问题解决，能够整合多种库，处理数据，执行 API 调用等；注重输出有意义的结果并进行分析和解释，必要时迭代代码)\n*   **代码风格/规范:** 偏向规范的开发方式，遵循 PEP 8 规范。倾向于使用设计模式来提高代码的拓展性和稳定性。注释风格偏向简洁，主要在代码段编写主题性注释（例如：描述核心功能或附加组件）。\n*   **代码组织方式:** 倾向于将核心能力封装成独立的第三方包，以提高灵活性。\n*   **文档习惯:** 会维护一些文档，但不会投入大量精力。\n*   **调试代码的方式:**\n    *   主要使用自动调试\n    *   不太擅长使用日志 (log)\n    *   更喜欢使用 `print` (调试时优先定位问题，会从程序入口开始，在关键节点打印 `print` 来锁定问题)\n    *   结合 `code_interpreter` 进行交互式调试\n*   **测试习惯:**\n    *   有编写测试用例的习惯\n    *   主要使用 `pytest`\n*   **代码重构:**\n    *   触发原因：代码质量差，维护和拓展性差\n    *   重构重点：提高代码质量、维护性和拓展性\n*   **工作流程:**\n    *   先进行设计\n    *   采用敏捷开发，不断迭代原型 (在原型阶段，框架、函数和想法可能不确定，重点是快速做出东西并根据结果进行修改)\n    *   再进行工程化开发\n*', mimetype='text/plain', start_char_idx=0, end_char_idx=1184, metadata_seperator='\n', text_template='{metadata_str}\n\n{content}'), score=0.7211514455077931),
     NodeWithScore(node=TextNode(id_='eb8c25cb-35ea-4f6f-8a66-5e88258068da', embedding=None, metadata={'topic': '库的使用', 'status': None, 'creation_date': '2025-05-19 18:34:33', 'tags': None, 'link': ''}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node_id='d9e35c5a-6814-4820-b289-866758923239', node_type='4', metadata={'topic': '库的使用', 'status': None, 'creation_date': '2025-05-19 18:34:33', 'tags': None, 'link': ''}, hash='5fbbec3e0fc213ebf6601e5dc1c516808d7d57dcf6fa44c6b4ba56215d9e68ec'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node_id='5d436a50-9940-4736-b550-67150433b0d0', node_type='1', metadata={}, hash='69738bf6c1376bfa4525d29d04967d6ec2d6703f68a7c99dfd5b33a9e24c11e1')}, metadata_template='{key}: {value}', metadata_separator='\n', text='topic: 库的使用 content: \n\n\n好的，没问题。根据我们之前讨论的内容和你的补充，我已经收集了足够的信息来为你整理一份关于 `llmada` 包（特别是 `BianXieAdapter`）的个人编程习惯记录。我将按照你的指示，只进行记录和总结，不会在 Code Interpreter 中执行代码。\n\n以下是根据我们的交流整理的你的个人编程习惯记录：\n\n---\n\n**个人编程习惯记录：`llmada` 包（特别是 `BianXieAdapter`）使用**\n\n**核心库:** `llmada` 包，提供与语言模型 API 交互的适配器。\n\n**核心组件:** `BianXieAdapter` 类，用于与 BianXie AI API 进行交互。\n\n**实例化习惯:**\n\n*   通常在需要使用时直接创建 `BianXieAdapter` 的新实例，例如 `bx = BianXieAdapter()`。\n*   API Key 的配置方式：\n    *   优先通过环境变量 `BIANXIE_API_KEY` 设置。\n    *   也支持在初始化时通过参数 `api_key` 传入。\n*   API Base URL 默认为 "https://api.bianxie.ai/v1/chat/completions"，通常不进行修改。\n\n**模型和参数设置习惯:**\n\n*   `self.model_pool` 中包含了非常丰富的模型列表，涵盖了多种模型提供商。\n*   **Temperature:** 很少手动设置 `temperature` 参数，倾向于使用默认值 0.7。认为温度对大部分任务影响不大，或更倾向于依赖 prompt 来控制输出风格。\n*   **模型选择:** 具体最常用的模型尚不明确，但知道有大量的模型可供选择，并根据任务场景可能选择不同的模型。\n\n**主要方法使用习惯:**\n\n*   **`product(prompt: str) -> str`:**\n    *   用于单轮问答或基于一个 prompt 生成文本。\n    *   常见使用场景包括信息提取（如 `extra_text` 函数中的例子）、文本生成等。\n    *   Prompt 的构建通常结合其他库（如 `promptlibz`）使用模板进行参数化。\n*   **`chat(messages: list) -> str`:**\n    *   用于多轮对话，接受一个包含消息字典的列表。\n    *   构建 `messages` 列表时，会包含用户和助手消息，可能使用 system 消息来设置对话上下文。\n*   **`product_stream(prompt: str) -> str` (Generator):**\n    *   支持流式输出，用于单轮问答。\n    *   在需要实时展示生成过程或处理大型输出时使用。\n*   **`chat_stream(messages: list) -> str` (Generator):**\n    *   支持流式输出，用于多轮对话。\n    *   在需要实时展示对话生成过程时使用。\n*   **`product_modal(prompt: RichPromptTemplate) -> str`:**\n    *   用于处理 `RichPromptTemplate` 类型的提示，可能涉及多模态或其他复杂提示结构。\n    *   使用场景相对较少或特定。\n*   **`set_model(model_name: str)`:** 用于动态切换模型，但使用频率相对较低，可能更倾向于在代码逻辑中根据任务固定使用某个模型。\n*   **`get_model() -> list[str]`:**', mimetype='text/plain', start_char_idx=0, end_char_idx=1599, metadata_seperator='\n', text_template='{metadata_str}\n\n{content}'), score=0.7208659709500019),
     NodeWithScore(node=TextNode(id_='f310d7be-885d-4609-98a0-5bef4ac80c3e', embedding=None, metadata={'topic': 'mermaid', 'status': None, 'creation_date': '2025-05-19 18:34:38', 'tags': ['python'], 'link': ''}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node_id='d0036b88-1eac-4fa1-9089-c8c01ea44728', node_type='4', metadata={'topic': 'mermaid', 'status': None, 'creation_date': '2025-05-19 18:34:38', 'tags': ['python'], 'link': ''}, hash='ad69cbae75958017227fb1c8f9b4ad86188583eaae1ece30cdb395d7c2a13ace'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node_id='b45c9085-b318-4c19-a823-6df1f6c16893', node_type='1', metadata={}, hash='4e557c68971b815628e1ff8ad9c0631f2c543520725607fa57c0e87f66e4308f')}, metadata_template='{key}: {value}', metadata_separator='\n', text='topic: mermaid content: \n\n\n### 个人习惯记录：编程场景下的 Mermaid 使用\n\n**核心理念：**\n\n- 将 Mermaid 作为一种结构化的二维关系表示方式，以便大模型（以及自己）更有效地理解和处理信息。\n- 重点在于关系本身的清晰表达，而非图的美观性。\n\n**主要工具和平台：**\n\n- **Mermaid：** 用于通过简洁的文本语法定义二维关系图。\n- **Obsidian Canvas：** 作为主要的**人类交互界面**，用于进行任务分解的初步可视化设计和对大模型优化结果的可视化展示。\n- **大模型：** 核心功能在于**理解**由 Mermaid 表示的图结构，并根据特定要求进行**优化和更新**，实现人机协作。\n- **NetworkX (潜在结合)：** 可能用于对 Mermaid 定义的图结构进行更深入的**分析**。\n\n**主要使用场景：**\n\n- **任务分解和规划：** 将复杂的任务分解为子任务，并梳理它们之间的依赖关系和顺序，用于项目管理和个人规划。\n- **理解和处理二维关系：** 不仅限于任务，也可能用于表示概念之间的关系、代码模块之间的依赖等。\n\n**主要图表类型：**\n\n- **有向图 (Directed Graph)：** 主要用于表示单向的影响、依赖或流程方向。\n\n**使用方式：**\n\n- **简单使用：** 侧重于使用基本的节点和连接线，不追求复杂的样式、标签、子图等高级功能。目的是为了**最大化转化效率和易读性**，方便人与大模型之间的交互。\n- **直接在 Obsidian 中使用：** 在 Markdown 笔记中直接书写 Mermaid 代码块。\n\n**与大模型的交互模式：**\n\n- **输入：** 直接将 Obsidian 中的 Mermaid 代码块输入给大模型。\n- **输出：** 期望大模型输出优化或更新后的 Mermaid 代码块。\n- **期望大模型的理解和处理能力：**\n    - **理解图的结构：** 识别节点、连接、方向等。\n    - **根据要求优化或更新图：** 例如，分解任务、调整依赖、建议并行化等。\n    - **实现与人类的交流：** 通过图的修改来体现理解和建议。\n\n**与 Obsidian Canvas 的工作流：**\n\n- **画布初步设计 (人类)：** 在 Canvas 中直观地绘制任务分解的初步结构。\n- **转化为 Mermaid (工具/脚本/手动)：** 将 Canvas 的视觉结构转化为简洁的 Mermaid 代码。\n- **大模型优化 (大模型)：** 将 Mermaid 代码输入大模型进行处理。\n- **转化为 Canvas (工具/脚本/手动)：** 将大模型优化后的 Mermaid 代码转化回 Canvas 进行可视化展示。\n- **人类继续操作和交互 (人类)：** 在 Canvas 中查看、修改并继续迭代。\n\n**选择 Mermaid 的原因：**\n\n- **语法简洁易懂：** 方便快速书写和理解。\n- **主流工具：** 广泛应用，大模型的训练集中包含大量 Mermaid 相关数据，对 Markdown 语法理解良好。\n-', mimetype='text/plain', start_char_idx=0, end_char_idx=1360, metadata_seperator='\n', text_template='{metadata_str}\n\n{content}'), score=0.7168775125152664),
     NodeWithScore(node=TextNode(id_='b45c9085-b318-4c19-a823-6df1f6c16893', embedding=None, metadata={'topic': 'mermaid', 'status': None, 'creation_date': '2025-05-19 18:34:38', 'tags': ['python'], 'link': ''}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node_id='d0036b88-1eac-4fa1-9089-c8c01ea44728', node_type='4', metadata={'topic': 'mermaid', 'status': None, 'creation_date': '2025-05-19 18:34:38', 'tags': ['python'], 'link': ''}, hash='ad69cbae75958017227fb1c8f9b4ad86188583eaae1ece30cdb395d7c2a13ace'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node_id='f310d7be-885d-4609-98a0-5bef4ac80c3e', node_type='1', metadata={'topic': 'mermaid', 'status': None, 'creation_date': '2025-05-19 18:34:38', 'tags': ['python'], 'link': ''}, hash='4b66706420b2e2db9de7c71ec24a96d954778480892f152596c5d39c1697803a')}, metadata_template='{key}: {value}', metadata_separator='\n', text='Mermaid 相关数据，对 Markdown 语法理解良好。\n- **适合表达二维关系：** 能够清晰地表示节点和它们之间的连接。\n\n**潜在需求：**\n\n- 对 Mermaid 的 Git 图表类型有兴趣，可能会在未来应用于代码版本管理和协作场景。\n\n**挑战和优化方向 (推测)：**\n\n- **Canvas 到 Mermaid，Mermaid 到 Canvas 的转化工具：** 目前的转化效率和准确性可能需要提升。\n- **大模型对复杂语义的理解：** 如何让大模型不仅仅理解图的结构，还能理解节点和边中蕴含的特定任务或概念的含义，以便进行更智能的优化。\n- **大模型生成 Mermaid 代码的准确性和规范性：** 如何确保大模型生成的代码符合 Mermaid 语法，并且能够被 Canvas 正确解析。\n\n---', mimetype='text/plain', start_char_idx=1327, end_char_idx=1691, metadata_seperator='\n', text_template='{metadata_str}\n\n{content}'), score=0.7141233024626293)]



## update


```python
query.update('我的汉王') # 想做一个metedata
```

## tools


```python
query.tools('kv.html')
```
