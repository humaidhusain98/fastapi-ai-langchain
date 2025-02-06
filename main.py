from dotenv import load_dotenv
from fastapi import FastAPI
from .routers import models,device,rag

load_dotenv() 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "server started on port 8000"}

app.include_router(models.router)
app.include_router(device.router)
app.include_router(rag.router)
