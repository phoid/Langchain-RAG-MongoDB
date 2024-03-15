# Langchain-RAG-MongoDB
 
#This is the core components for a RAG Application using mongoDBAtlas, Langchain, and OpenAI.

The it is based on the following repo:

https://github.com/mongodb-developer/atlas-vector-search-rag

Major Changes:
- Updated Imports for langchain -> langchain_community
- Added functionality for PDF inputs
- Changed File read to be system agnostic and iterative.

To Run you will need:
- An env with requirements.txt
- A mongoDB URI
- An OpenAI Key 

