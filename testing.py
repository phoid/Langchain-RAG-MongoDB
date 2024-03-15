from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from langchain_community.llms import OpenAI
from langchain_community.document_loaders import PyPDFLoader


def process_pdf():
    loader = PyPDFLoader("pdfs\OCB-student-handbook-v3.6.pdf")
    pages = loader.load_and_split()
    print(pages[258].page_content)


process_pdf()
