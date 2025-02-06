import os
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import status
from ..models.response import Response
from ..models.testresponse import testRes

gemini_api_key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=gemini_api_key)

def generateModelAnswerFromStringPrompt(prompt):
    try:
        result = model.invoke(prompt)
        # result=  testRes(prompt)
        print(f'{result}')
        response = Response(status.HTTP_200_OK,"Successfully Generated Response",result.content); 
        print(response)
        return response
    except:
        print('Something Unexpected while generating prompt')
        response = Response(status.HTTP_500_INTERNAL_SERVER_ERROR,"UnExpected Error Occured","")
        return response