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

## 📦 Installation Instructions

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

## 🚀 Start Instructions
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

### 1. Signup(POST)

Signup API is used to register a new user from dashboard, once the new user enters the details and a request to signup API is post to make a database entry for this new user created.

**_Params_**

- userName
- password

**Endpoint**

```
http://localhost:3000/signup
```

### 2. Login(POST)

When a previous user login on the dashboard with the login details and post this login API request to fetch the details from backend and allow user to transact.

**_Params_**

- userName
- password

**Endpoint**

```
http://localhost:3000/login
```

### 3. Deploy Wallet(POST)

Deploy an CFA Account by sending a deploy post API request with passing the parameters Counter Factual (CFA address of user).

**_Params_**

- cfa

**Endpoint**

```
http://localhost:3000/deploy:cfa
```

### 4. Transfer Funds(POST)

Transfer of funds can be done by providing the params like To(to whom) address, Value(how much you send) and cfa(of the user who is sending the funds) and sending the post request.

**_Params_**

- to
- value
- cfa

**Endpoint**

```
http://localhost:3000/transferSCW
```


