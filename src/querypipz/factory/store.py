""" store factory """
from enum import Enum
from typing import Any
import os
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.vector_stores import SimpleVectorStore
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.graph_stores.nebula import NebulaPropertyGraphStore
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
from llama_index.graph_stores.memgraph import MemgraphPropertyGraphStore

from pinecone import Pinecone
import faiss








class VectorStoreType(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
    """
    SIMPLE_VECTOR_STORE = 'SimpleVectorStore'
    FAISS = 'FAISS'
    PINECONE = "PINECONE"
    PG_VECTOR_STORE = "pgVectorStore"
    # 添加更多选项

class VectorStore:
    """_summary_
    """
    def __new__(cls, vector_type: VectorStoreType) -> Any:
        assert vector_type.value in [i.value for i in VectorStoreType]
        instance = None

        if vector_type.value == 'SimpleVectorStore':
            instance = SimpleVectorStore()

        elif vector_type.value == 'FAISS':
            # Create a FAISS index
            faiss_index = faiss.IndexFlatL2(1536)  # Example dimension
            instance = FaissVectorStore(faiss_index=faiss_index)

        elif vector_type.value == 'PINECONE':
            # Create a FAISS index
            api_key = os.environ["PINECONE_API_KEY"]
            pc = Pinecone(api_key=api_key)
            pinecone_index = pc.Index("quickstart-index")
            vector_store = PineconeVectorStore(
                                            pinecone_index=pinecone_index, namespace="test_05_14"
                                        )
            instance = vector_store
        elif vector_type.value == "pgVectorStore":
            
            vector_store = PGVectorStore.from_params(
                database="vector_db",
                host=self.info.host,
                password=self.info.password,
                port=self.info.port,
                user=self.info.user,
                table_name=index_name,
                embed_dim=1536,  # openai embedding dimension
                hnsw_kwargs={
                    "hnsw_m": 16,
                    "hnsw_ef_construction": 64,
                    "hnsw_ef_search": 40,
                    "hnsw_dist_method": "vector_cosine_ops",
                    },
            )
            instance = vector_store

        else:
            raise TypeError('Unknown type')

        return instance


class DocStoreType(Enum):
    """Docs

    Args:
        Enum (_type_): _description_
    """
    SIMPLE_DOCUMENT_STORE = 'SimpleDocumentStore'
    # Add more options as needed


class DocStore:
    """DocStore
    """
    def __new__(cls, doc_type: DocStoreType) -> Any:
        assert doc_type.value in [i.value for i in DocStoreType]
        instance = None

        if doc_type.value == 'SimpleDocumentStore':
            instance = SimpleDocumentStore()
        else:
            raise TypeError('Unknown type')

        return instance


class GraphStoreType(Enum):
    """GraphStoreType

    Args:
        Enum (_type_): _description_
    """
    SIMPLE_GRAPH_STORE = 'SimpleGraphStore'
    NEBULA_GRAPH_STORE = 'NebulaGraphStore'
    NEO4J_GRAPH_STORE = 'Neo4jGraphStore'
    MEMGRAPH_GRAPH_STORE = 'MemgraphGraphStore'

class GraphStore:
    """GraphStore
    """
    def __new__(cls, graph_type: GraphStoreType) -> Any:
        assert graph_type.value in [i.value for i in GraphStoreType]
        instance = None

        if graph_type.value == 'SimpleGraphStore':
            instance = SimpleGraphStore()
        elif graph_type.value == 'NebulaGraphStore':
            os.environ["NEBULA_USER"] = "root"
            os.environ["NEBULA_PASSWORD"] = "nebula"
            os.environ["NEBULA_ADDRESS"] = "127.0.0.1:9669"
            # Initialize NebulaPropertyGraphStore
            graph_store = NebulaPropertyGraphStore(
                space="llamaindex",
                overwrite=True  # Overwrite existing space if needed
            )
            instance = graph_store


        elif graph_type.value == 'Neo4jGraphStore':
            graph_store = Neo4jPropertyGraphStore(
                username="neo4j",
                password="ZHF4233613",
                url="bolt://localhost:7687",
            )
            instance = graph_store

        elif graph_type.value == 'MemgraphGraphStore':
            graph_store = MemgraphPropertyGraphStore(
                username="",# Enter your Memgraph username (default "")
                password="",# Enter your Memgraph password (default "")
                url="",  # Specify the connection URL, e.g., 'bolt://localhost:7687'
            )
            instance = graph_store
        else:
            raise TypeError('Unknown type')

        return instance
