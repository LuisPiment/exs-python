from fastapi import FastAPI, Query,Body,HTTPException
from pydantic import BaseModel
from typing import Union,List,Set
app=FastAPI()
class morada(BaseModel):
    cidade:str
    pais:str
    continente:str
class Toma(BaseModel):
    Nome:str
    idade:int =None
    cidade: morada=None

@app.get("/items",tags=["items"])
def root(largura:int =0, comprimento:int =0):
    if largura>50 or comprimento>50:
        raise HTTPException(status_code=404,detail="O comprimento e a largura tem de ser menores que 50")
    else:
        area=largura*comprimento
        return(f"A area é {area} e os nomes são ")

@app.post("/pessoa",tags=["items"])
def caminho(toma:Toma,lingundo:int =0):
    return(toma.cidade)