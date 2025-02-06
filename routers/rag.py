from fastapi import APIRouter,Response
from ..langchain import embeddings
from pydantic import BaseModel

class Body(BaseModel):
    inputFileName:str
    outputFileName:str

router = APIRouter(
    prefix="/rag"
)

@router.post("/generateEmbeddingsFromTextFile")
async def generateEmbeddingsTxtFile(body:Body,response:Response):
    print(body)
    generatedResponse = embeddings.generateEmbeddingsFromTextFile(body.inputFileName,body.outputFileName)
    response.status_code=generatedResponse.httpCode
    return generatedResponse

