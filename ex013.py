from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Union
app=FastAPI()
class Toma(BaseModel):
    Nome:str
    idade:int =None
    cidade: Union[str,None]=None

@app.get("/items")
def root(largura:int =0, comprimento:int =0, altura:int =Query(default=None, max_digits=50)):
    area=largura*comprimento
    if altura!=0:
        volume=comprimento*altura*largura
        return(f"A area é {area} e o volume é {volume}")
    return(f"A area é {area}")

@app.post("/pessoa")
def dalhe(hmm:Toma):
    return hmm
