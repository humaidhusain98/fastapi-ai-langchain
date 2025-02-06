import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from ..models.response import Response
from fastapi import status

def generateEmbeddingsFromTextFile(inputFileName,outputFileName):
    try:
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, "rag_train_data", inputFileName)
        persistent_directory = os.path.join(current_dir, "emdeddings_db", outputFileName)

        # Check if the Chroma vector store already exists
        if not os.path.exists(persistent_directory):
            print("Persistent directory does not exist. Initializing vector store...")

            # Ensure the text file exists
            if not os.path.exists(file_path):
                response = Response(status.HTTP_404_NOT_FOUND,inputFileName+" not found","")
                return response
                # raise FileNotFoundError(
                #     f"The file {file_path} does not exist. Please check the path."
                # )

            # Read the text content from the file
            loader = TextLoader(file_path)
            documents = loader.load()

            # Split the document into chunks
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            docs = text_splitter.split_documents(documents)

            # Display information about the split documents
            print("\n--- Document Chunks Information ---")
            print(f"Number of document chunks: {len(docs)}")
            print(f"Sample chunk:\n{docs[0].page_content}\n")

            # Create embeddings
            print("\n--- Creating embeddings ---")
            embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small"
            )  # Update to a valid embedding model if needed
            print("\n--- Finished creating embeddings ---")

            # Create the vector store and persist it automatically
            print("\n--- Creating vector store ---")
            db = Chroma.from_documents(
                docs, embeddings, persist_directory=persistent_directory)
            print("\n--- Finished creating vector store ---")
            response = Response(status.HTTP_201_CREATED,"Successfully Created Vector Store","Chroma db written to "+persistent_directory)
            return response
        else:
            print("Vector store already exists. No need to initialize.")
            response = Response(status.HTTP_409_CONFLICT,"vetor store in "+outputFileName + "already exists","")
            return response
            
    except:
        response = Response(status.HTTP_500_INTERNAL_SERVER_ERROR,"Something unexpected occured","")
        return response

