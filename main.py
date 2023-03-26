from fastapi import FastAPI,Request
from fakerweb.fakerweb import runner
from pydantic import BaseModel


app = FastAPI()


class BaseClassModel(BaseModel):
    entity:str
    
class NameModel(BaseClassModel):
    fname_only: str
    prefix :str


class MainModel(BaseClassModel):
    test: NameModel

@app.get("/api/random")
async def get_random(request: Request):
    
    return runner(await request.json())

@app.get("/api/test")
async def get_random(data: MainModel):
    
    return "test"
