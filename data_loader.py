from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import PGVector
from rich import print
import requests
import os

loader = CSVLoader(file_path='seed_data/mobile_recommendation_system_dataset.csv',
    metadata_columns=("name","imgURL"),
    csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['name','ratings','price','imgURL','corpus']
})
docs = loader.load()

embeddings = HuggingFaceEmbeddings()

CONNECTION_STRING = "postgresql+psycopg://postgres:password@localhost:5432/vectordb"
COLLECTION_NAME = "mobile_phones"

db = PGVector.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
    use_jsonb=True,
    # pre_delete_collection=True # This deletes existing collection and its data, use carefully!
)
