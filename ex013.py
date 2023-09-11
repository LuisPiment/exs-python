from fastapi import FastAPI, Query,Body
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

@app.get("/items")
def root(largura:int =0, comprimento:int =Query(gt=50,lt=90) ):
    area=largura*comprimento
    return(f"A area é {area} e os nomes são ")

@app.post("/pessoa")
def caminho(toma:Toma,lingundo:int =0):
    return(toma.cidade)