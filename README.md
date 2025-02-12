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
- [All Endpoints ](#all-endpoints)
	- [1. Server Check API](#1-server-check-api)
	- [2. Models : GPT 4o MINI API](#2-models--gpt-4o-mini-api)
 	- [3. Models : GEMINI 1.5 PRO API](#3-models--gemini-15-pro-api)
  	- [4. RAG Embeddings Generation from Text File](#4-rag-embeddings-generation-from-text-file)
  	- [5. RAG Retrieval From Existing Chroma DB Vector Store Generated Previously](#5-rag-retrieval-from-existing-chroma-db-vector-store-generated-previously)
  	- [6. Generate Response From GPT-4-MINI MODEL after Data Retrieval From RAG Vector Store](#6-generate-response-from-gpt-4-mini-model-after-data-retrieval-from-rag-vector-store)
 	

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

## All Endpoints

### 1. Server Check API

This api is used to check if the server is running correctly.

**HTTP Method Type** : GET

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

### 2. Models : GPT 4o MINI API

This api exposes OpenAI's chatgpt-4o-mini model to be invoked and consumed by Applications. It takes the prompt in the request body and generates a response by the gpt-4o-mini model and returns back the results.

**HTTP Method Type** : POST

**Request Body Fields**

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
### 3. Models : GEMINI 1.5 PRO API

This api exposes Gemini 1.5 Pro model to be invoked and consumed by Applications. It takes the prompt in the request body and generates a response by the gpt-4o-mini model and returns back the results.

**HTTP Method Type** : POST

**Request Body Fields**
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

This api is used to generate embeddings from a text file and store the embeddings vector store in chroma db inside the embeddings_db/{outputFolderName} folder. The api fetches the file from the rag_train_data/{inputFileName}.txt file and creates embeddings using the  . To generate the embeddings we use OpenAI's text-embedding-3-small model  

**HTTP Method Type** : POST

**Request Body Fields**

- inputFileName
- outputFolderName

**Endpoint**

```
http://localhost:8000/rag/generateEmbeddingsFromTextFile
```

**Curl Example**
```curl
curl --location 'http://localhost:8000/rag/generateEmbeddingsFromTextFile' \
--header 'Content-Type: application/json' \
--data '{
    "inputFileName":"sample_training_file.txt",
    "outputFolderName":"chroma_db"
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
    "msg": "vetor store in chroma_db already exists",
    "data": ""
}
```

**Sample Successful Response**
```json
{
    "httpCode": 201,
    "msg": "Successfully Created Vector Store",
    "data": "Chroma db written to /Users/mdhumaidhusain/python-ai/fastapi-server/emdeddings_db/chroma_db"
}
```

### 5. RAG Retrieval From Existing Chroma DB Vector Store Generated Previously

This api is used to retrieve data from previously created Chroma DB vector store. It takes in the query, vector_store_name, search_type and search_kwargs in the request body and fetches the document based on the search_type and search_kwarrgs specified .The api supports different retrieval methods like Similarity Search,  Max Marginal Relevance (MMR) and Similarity Score Threshold.

**HTTP Method Type** : POST

**Request Body Fields**

- query
- vector_store_name
- search_type
- search_kwargs

**Endpoint**

```
http://localhost:8000/rag/retrieveRagDataFromVectorStore
```

**Search Types**
1. Similarity Search: This method retrieves documents based on vector similarity. It finds the most similar documents to the query vector based on cosine similarity. Use this when you want to retrieve the top k most similar documents.

**Similarity Search Example Curl and Response**
<br/>
Curl:

```curl
curl --location 'http://localhost:8000/rag/retrieveRagDataFromVectorStore' \
--header 'Content-Type: application/json' \
--data '{
    "query":"Who is Odysseus wife?",
    "vector_store_name":"chroma_db",
    "search_type":"similarity",
    "search_kwargs":{"k": 3}
}'
```
Response:
```json
{
    "httpCode": 200,
    "msg": "Successfully Retrieved from Vector Store",
    "data": [
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "“Happy Ulysses, son of Laertes,” replied the ghost of Agamemnon, “you\nare indeed blessed in the possession of a wife endowed with such rare\nexcellence of understanding, and so faithful to her wedded lord as\nPenelope the daughter of Icarius. The fame, therefore, of her virtue\nshall never die, and the immortals shall compose a song that shall be\nwelcome to all mankind in honour of the constancy of Penelope. How far\notherwise was the wickedness of the daughter of Tyndareus who killed\nher lawful husband; her song shall be hateful among men, for she has\nbrought disgrace on all womankind even on the good ones.”",
            "type": "Document"
        },
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "Then Ulysses answered, “Madam, wife of Ulysses, you need not defer your\ntournament, for Ulysses will return ere ever they can string the bow,\nhandle it how they will, and send their arrows through the iron.”\n\nTo this Penelope said, “As long, sir, as you will sit here and talk to\nme, I can have no desire to go to bed. Still, people cannot do\npermanently without sleep, and heaven has appointed us dwellers on\nearth a time for all things. I will therefore go upstairs and recline\nupon that couch which I have never ceased to flood with my tears from\nthe day Ulysses set out for the city with a hateful name.”\n\nShe then went upstairs to her own room, not alone, but attended by her\nmaidens, and when there, she lamented her dear husband till Minerva\nshed sweet sleep over her eyelids.\n\n\nBOOK XX",
            "type": "Document"
        },
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "This was what they said, but they did not know what it was that had\nbeen happening. The upper servant Eurynome washed and anointed Ulysses\nin his own house and gave him a shirt and cloak, while Minerva made him\nlook taller and stronger than before; she also made the hair grow thick\non the top of his head, and flow down in curls like hyacinth blossoms;\nshe glorified him about the head and shoulders just as a skilful\nworkman who has studied art of all kinds under Vulcan or Minerva—and\nhis work is full of beauty—enriches a piece of silver plate by gilding\nit. He came from the bath looking like one of the immortals, and sat\ndown opposite his wife on the seat he had left. “My dear,” said he,\n“heaven has endowed you with a heart more unyielding than woman ever\nyet had. No other woman could bear to keep away from her husband when\nhe had come back to her after twenty years of absence, and after having\ngone through so much. But come, nurse, get a bed ready for me; I will\nsleep alone, for this woman has a heart as hard as iron.”",
            "type": "Document"
        }
    ]
}
```

2. Max Marginal Relevance (MMR): This method balances between selecting documents that are relevant to the query and diverse among themselves. 'fetch_k' specifies the number of documents to initially fetch based on similarity. 'lambda_mult' controls the diversity of the results: 1 for minimum diversity, 0 for maximum. Use this when you want to avoid redundancy and retrieve diverse yet relevant documents.
Note: Relevance measures how closely documents match the query. Diversity ensures that the retrieved documents are not too similar to each other, providing a broader range of information.
**Similarity Search Example Curl and Response**
<br/>
Curl:

```curl
curl --location 'http://localhost:8000/rag/retrieveRagDataFromVectorStore' \
--header 'Content-Type: application/json' \
--data '{
    "query":"Who is Odysseus wife?",
    "vector_store_name":"chroma_db",
    "search_type":"mmr",
    "search_kwargs": {"k": 3, "fetch_k": 20, "lambda_mult": 0.5}
}'
```
Response:
```json
{
    "httpCode": 200,
    "msg": "Successfully Retrieved from Vector Store",
    "data": [
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "“Happy Ulysses, son of Laertes,” replied the ghost of Agamemnon, “you\nare indeed blessed in the possession of a wife endowed with such rare\nexcellence of understanding, and so faithful to her wedded lord as\nPenelope the daughter of Icarius. The fame, therefore, of her virtue\nshall never die, and the immortals shall compose a song that shall be\nwelcome to all mankind in honour of the constancy of Penelope. How far\notherwise was the wickedness of the daughter of Tyndareus who killed\nher lawful husband; her song shall be hateful among men, for she has\nbrought disgrace on all womankind even on the good ones.”",
            "type": "Document"
        },
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "On this she came down from her upper room, and while doing so she\nconsidered whether she should keep at a distance from her husband and\nquestion him, or whether she should at once go up to him and embrace\nhim. When, however, she had crossed the stone floor of the cloister,\nshe sat down opposite Ulysses by the fire, against the wall at right\nangles180 [to that by which she had entered], while Ulysses sat near\none of the bearing-posts, looking upon the ground, and waiting to see\nwhat his brave wife would say to him when she saw him. For a long time\nshe sat silent and as one lost in amazement. At one moment she looked\nhim full in the face, but then again directly, she was misled by his\nshabby clothes and failed to recognise him,181 till Telemachus began to\nreproach her and said:",
            "type": "Document"
        },
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "So now all who escaped death in battle or by shipwreck had got safely\nhome except Ulysses, and he, though he was longing to return to his\nwife and country, was detained by the goddess Calypso, who had got him\ninto a large cave and wanted to marry him. But as years went by, there\ncame a time when the gods settled that he should go back to Ithaca;\neven then, however, when he was among his own people, his troubles were\nnot yet over; nevertheless all the gods had now begun to pity him\nexcept Neptune, who still persecuted him without ceasing and would not\nlet him get home.",
            "type": "Document"
        }
    ]
}
```
3. Similarity Score Threshold: This method retrieves documents that exceed a certain similarity score threshold. 'score_threshold' sets the minimum similarity score a document must have to be considered relevant. Use this when you want to ensure that only highly relevant documents are retrieved, filtering out less relevant ones.

**Similarity Search Example Curl and Response**
<br/>
Curl:

```curl
curl --location 'http://localhost:8000/rag/retrieveRagDataFromVectorStore' \
--header 'Content-Type: application/json' \
--data '{
    "query":"Who is Odysseus wife?",
    "vector_store_name":"chroma_db",
    "search_type":"similarity_score_threshold",
    "search_kwargs":{"k": 5, "score_threshold": 0.4}
}'
```
Response:
```json
{
    "httpCode": 200,
    "msg": "Successfully Retrieved from Vector Store",
    "data": [
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "“Happy Ulysses, son of Laertes,” replied the ghost of Agamemnon, “you\nare indeed blessed in the possession of a wife endowed with such rare\nexcellence of understanding, and so faithful to her wedded lord as\nPenelope the daughter of Icarius. The fame, therefore, of her virtue\nshall never die, and the immortals shall compose a song that shall be\nwelcome to all mankind in honour of the constancy of Penelope. How far\notherwise was the wickedness of the daughter of Tyndareus who killed\nher lawful husband; her song shall be hateful among men, for she has\nbrought disgrace on all womankind even on the good ones.”",
            "type": "Document"
        },
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "Then Ulysses answered, “Madam, wife of Ulysses, you need not defer your\ntournament, for Ulysses will return ere ever they can string the bow,\nhandle it how they will, and send their arrows through the iron.”\n\nTo this Penelope said, “As long, sir, as you will sit here and talk to\nme, I can have no desire to go to bed. Still, people cannot do\npermanently without sleep, and heaven has appointed us dwellers on\nearth a time for all things. I will therefore go upstairs and recline\nupon that couch which I have never ceased to flood with my tears from\nthe day Ulysses set out for the city with a hateful name.”\n\nShe then went upstairs to her own room, not alone, but attended by her\nmaidens, and when there, she lamented her dear husband till Minerva\nshed sweet sleep over her eyelids.\n\n\nBOOK XX",
            "type": "Document"
        },
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "This was what they said, but they did not know what it was that had\nbeen happening. The upper servant Eurynome washed and anointed Ulysses\nin his own house and gave him a shirt and cloak, while Minerva made him\nlook taller and stronger than before; she also made the hair grow thick\non the top of his head, and flow down in curls like hyacinth blossoms;\nshe glorified him about the head and shoulders just as a skilful\nworkman who has studied art of all kinds under Vulcan or Minerva—and\nhis work is full of beauty—enriches a piece of silver plate by gilding\nit. He came from the bath looking like one of the immortals, and sat\ndown opposite his wife on the seat he had left. “My dear,” said he,\n“heaven has endowed you with a heart more unyielding than woman ever\nyet had. No other woman could bear to keep away from her husband when\nhe had come back to her after twenty years of absence, and after having\ngone through so much. But come, nurse, get a bed ready for me; I will\nsleep alone, for this woman has a heart as hard as iron.”",
            "type": "Document"
        },
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "Euryclea now went upstairs laughing to tell her mistress that her dear\nhusband had come home. Her aged knees became young again and her feet\nwere nimble for joy as she went up to her mistress and bent over her\nhead to speak to her. “Wake up Penelope, my dear child,” she exclaimed,\n“and see with your own eyes something that you have been wanting this\nlong time past. Ulysses has at last indeed come home again, and has\nkilled the suitors who were giving so much trouble in his house, eating\nup his estate and ill treating his son.”",
            "type": "Document"
        },
        {
            "id": null,
            "metadata": {
                "source": "/Users/mdhumaidhusain/python-ai/new-lang/fastapi-ai-langchain/rag_train_data/odyssey.txt"
            },
            "page_content": "Many a plausible tale did Ulysses further tell her, and Penelope wept\nas she listened, for her heart was melted. As the snow wastes upon the\nmountain tops when the winds from South East and West have breathed\nupon it and thawed it till the rivers run bank full with water, even so\ndid her cheeks overflow with tears for the husband who was all the time\nsitting by her side. Ulysses felt for her and was sorry for her, but he\nkept his eyes as hard as horn or iron without letting them so much as\nquiver, so cunningly did he restrain his tears. Then, when she had\nrelieved herself by weeping, she turned to him again and said: “Now,\nstranger, I shall put you to the test and see whether or no you really\ndid entertain my husband and his men, as you say you did. Tell me,\nthen, how he was dressed, what kind of a man he was to look at, and so\nalso with his companions.”",
            "type": "Document"
        }
    ]
}
```


### 6. Generate Response From GPT-4-MINI MODEL after Data Retrieval From RAG Vector Store

This api is used to generate a answer from gpt-4o-mini model after we retrieve relevant data from the vector store using the retrieval methods discussed in the above apis.

**HTTP Method Type** : POST

**Request Body Fields**

- query
- vector_store_name
- search_type
- search_kwargs

**Endpoint**

```
http://localhost:8000/rag/generateGPT-4o-miniRAG
```

**Curl Example and Response**
<br/>
Curl:
```curl
curl --location 'http://localhost:8000/rag/generateGPT-4o-miniRAG' \
--data '{
    "query":"Who is Odysseus wife?",
    "vector_store_name":"chroma_db",
    "search_type":"mmr",
    "search_kwargs": {"k": 3, "fetch_k": 20, "lambda_mult": 0.5}
}'
```
Response:
```json
{
    "httpCode": 200,
    "msg": "Successfully Retrieved response from ChatGPT",
    "data": "Odysseus's wife is Penelope, the daughter of Icarius."
}
```



