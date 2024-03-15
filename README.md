# Langchain-RAG-MongoDB
 
#This is the core components for a RAG Application using mongoDBAtlas(Database+RAG), Langchain(CORE + API), OpenAI(MODELS), and Gradio(Frontend)

The it is based on the following repo:

https://github.com/mongodb-developer/atlas-vector-search-rag

Major Changes:
- Updated Imports for langchain -> langchain_community
- Added functionality for PDF inputs
- Changed File read to be system agnostic and iterative.
- Added a Free Marine biology 101 sample to test the application on.

To Run you will need:
- An env with requirements.txt
- A mongoDB URI
- An OpenAI Key 

