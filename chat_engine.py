from langchain.chains import RetrievalQA
from langchain.llms import Ollama

def build_chat_chain(vector_store):
    llm = Ollama(model='llama3')
    return RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever())

# from langchain.chains import RetrievalQA
# from langchain.llms import Ollama

# def build_chat_chain(vector_store):
#     llm = Ollama(model="llama3")
#     retriever = vector_store.as_retriever()
#     qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
#     return qa_chain
