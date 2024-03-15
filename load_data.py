from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from langchain_community.llms import OpenAI
import keys
import getpass
import os
from langchain_community.document_loaders import PyPDFLoader


# os.environ[keys.OPENAI_KEY] = getpass.getpass()

directory = os.fsencode("samples")

# Set the MongoDB URI, DB, Collection Names

client = MongoClient(keys.MONGO_URI)
database = client["langchain"]
collection = database["Docs"]

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=keys.OPENAI_KEY,
    dimensions=1516,
)


def process_text_file():
    for file in os.scandir(directory):

        file = open(file, encoding="utf8")
        text_content = file.read()
        embedded = embeddings.embed_query(text_content)
        document = {
            "text": text_content,
            "embedding": embedded,
        }
        collection.insert_one(document)


def process_pdf():
    loader = PyPDFLoader("pdfs\OCB-student-handbook-v3.6.pdf")
    pages = loader.load_and_split()
    for page in pages:
        embedded = embeddings.embed_query(page.page_content)
        document = {
            "text": page.page_content,
            "embedding": embedded,
        }
        collection.insert_one(document)


process_text_file()

process_pdf()


def text_to_embedding(text):
    return embeddings.embed_query(text)


# # Store embeddings in MongoDB alongside your documents
# for doc in collection.find():
#     embedding = text_to_embedding(doc["text_content"])
#     collection.update_one(
#         {"_id": doc["_id"]}, {"$set": {"embedding": embedding.tolist()}}
#     )


# Vector search
def search_by_vector(query_text, top_n=3):
    query_embedding = text_to_embedding(query_text)

    results = collection.find(
        {
            "embedding": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": query_embedding.tolist(),
                    },
                    "$maxDistance": 1000,  # Adjust threshold as needed
                }
            }
        }
    )

    return list(results)[:top_n]
