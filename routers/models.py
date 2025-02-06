from fastapi import APIRouter,Response
from ..langchain import openai, gemini
from pydantic import BaseModel

class Prompt(BaseModel):
    data: str

router = APIRouter(
    prefix="/models"
)

@router.post("/gpt-4o-mini")
async def generateGPT4Query(prompt:Prompt,response:Response):
    print(prompt)
    generatedResponse = openai.generateModelAnswerFromStringPrompt(prompt=prompt.data)
    response.status_code=generatedResponse.httpCode
    return generatedResponse

@router.post("/gemini-1.5-pro")
async def generateGeminiQuery(prompt:Prompt,response:Response):
    print(prompt)
    generatedResponse = gemini.generateModelAnswerFromStringPrompt(prompt=prompt.data)
    response.status_code=generatedResponse.httpCode
    return generatedResponse
        
