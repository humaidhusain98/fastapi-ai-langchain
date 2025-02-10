from langchain_openai import ChatOpenAI
from fastapi import status
from ..models.response import Response
from ..models.testresponse import testRes

model = ChatOpenAI(model="gpt-4o-mini")

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
