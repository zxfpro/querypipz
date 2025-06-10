""" useful tools """

class VisualIndex():
    """visualization Index
    """
    def __init__(self,index):
        self.index = index

    def get_docs_id(self):
        """ get docs ids """
        return list(self.index.docstore.docs.keys())

    def get_documents(self):
        """ get documents """
        return [self.index.docstore.get_document(i) for i in self.get_docs_id()]

    def get_document_by_id(self,doc_id): # 有a功能
        """ get documents by doc_id """
        return self.index.docstore.get_document(doc_id)
