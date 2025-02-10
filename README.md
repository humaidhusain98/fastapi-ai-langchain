# fastapi-ai-langchain
This Repository contains a Fastapi server which has apis to use models like chatgpt and gemini using Langchain. It also has apis for RAG embeddings generation on custom data and storing it to ChromaDB for later use


# 🚀 FastAPI Project

---

## 🛠 Features
- 🔗 RESTful APIs with FastAPI
- 📜 Auto-generated Swagger & ReDoc API documentation
- 🗄️ Database integration with migrations support
- 🧪 Ready for development and production setups

---
## Table of Contents

- [Installation Instructions](#installation-instructions)
- [Start Instructions](#start-instructions)
- [All Endpoints - Required params](#all-endpoints---required-params)

## Installation Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:humaidhusain98/fastapi-ai-langchain.git
cd fastapi-ai-langchain
```

### 2. Create a Virtual Environment
It's best practice to create a virtual environment for your Python projects:
```bash
python3 -m venv env
# Activate the virtual environment
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages using pip and the requirements.txt
```bash
pip install -r requirements.txt
```

### 4.Set Up Environment Variables
Create a .env file in the root directory and add the details given in the .env.example file and fill the details. 
<br />
1. OpenAI API Key: Go to https://platform.openai.com/ and generate an API key
2. Gemini API Key: Go to https://aistudio.google.com/app/apikey and generate an API key
```env
OPENAI_API_KEY=
GEMINI_API_KEY=
```

## Start Instructions
### 1. Run the FastAPI Development Server
Use the following command in root folder terminal to run the development server
```bash
fastapi dev main.py
```

### 2. Access the API
Once the server is running, the API will be available at:
```arduino
http://127.0.0.1:8000
```

### 3. Explore the Documentation
FastAPI automatically generates interactive API docs:
- Swagger UI: http://127.0.0.1:8000/docs

### 4. Run the Production Server
Use the following command in root folder terminal to run the production server
```bash
fastapi run main.py
```

## All Endpoints - Required params

### 1. Server Check(GET)

This api is used to check if the server is running correctly.


**Endpoint**

```
http://localhost:8000
```

**Response**
<br/>
It will display the following JSON Response
```json
{"message": "server started on port 8000"}
```

### 2. Models : GPT 4o MINI API(POST)

This api exposes OpenAI's chatgpt-4o-mini model to be invoked and consumed by Applications. It takes the prompt in the request body and generates a response by the gpt-4o-mini model and returns back the results.

**_Params_**

- prompt

**Endpoint**

```
http://localhost:8000/models/gpt-4o-mini
```

**Curl Example**
```curl
curl --location 'http://localhost:8000/models/gpt-4o-mini' \
--header 'Content-Type: application/json' \
--data '{
	"prompt": "What is 81 divided by 9"
}'
``` 

**Example Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": "81 divided by 9 is 9"
}
```
### 3. Models : GEMINI 1.5 PRO API(POST)

This api exposes Gemini 1.5 Pro model to be invoked and consumed by Applications. It takes the prompt in the request body and generates a response by the gpt-4o-mini model and returns back the results.

**_Params_**

- prompt

**Endpoint**

```
http://localhost:8000/models/gemini-1.5-pro
```

**Curl Example**
```curl
curl --location 'http://localhost:8000/models/gemini-1.5-pro' \
--header 'Content-Type: application/json' \
--data '{
	"prompt": "What is 81 divided by 9"
}'
``` 

**Example Response**
```json
{
    "httpCode": 200,
    "msg": "Successfully Generated Response",
    "data": "81 divided by 9 is 9"
}
```

### 4. RAG Embeddings Generation from Text File

This api is used to generate embeddings from a text file and store the embeddings vector store in chroma db inside the embeddings_db/{outputFileName} folder. The api fetches the file from the rag_train_data/{inputFileName}.txt file and creates embeddings using the  . To generate the embeddings we use OpenAI's text-embedding-3-small model  

**_Params_**

- inputFileName
- outputFileName

**Endpoint**

```
http://localhost:8000/rag/generateEmbeddingsFromTextFile
```

**Curl Example**
```curl
curl --location 'http://localhost:8000/rag/generateEmbeddingsFromTextFile' \
--header 'Content-Type: application/json' \
--data '{
    "inputFileName":"odyssey.txt",
    "outputFileName":"chroma_db"
}'
```
**Sample File Not Found Response**
```json
{
    "httpCode": 404,
    "msg": "dasd.txt not found",
    "data": ""
}
```
**Sample Vector Store Already Exists for output name Response**
```json
{
    "httpCode": 409,
    "msg": "vetor store in chroma_dbalready exists",
    "data": ""
}
```

**Sample Successful Response **
```json
{
    "httpCode": 201,
    "msg": "Successfully Created Vector Store",
    "data": "Chroma db written to /Users/mdhumaidhusain/python-ai/fastapi-server/emdeddings_db/chroma_db"
}
```

