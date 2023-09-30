from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
app=FastAPI()

class Certificado(BaseModel):
    nome:str
    idade:int
    descrição:Union[str,int,None]=False
    morada:Union[str,int]

@app.post("/formula")
def forma (item:Certificado):
    if item.descrição==False:
        return(f"nome:{item.nome}  "
               f"idade:{item.idade}  "
               f"morada:{item.morada}  ")
    else:
        return(f"nome:{item.nome}  "
               f"idade:{item.idade}  "
               f"descrição:{item.descrição}  "
               f"morada:{item.morada}   ")
           



@app.get("/bola")
def bola(comprimento:int=90,largura:int=80,altura:int | None=False):
    area=comprimento*largura
    if altura==False:
        return(f"A area é {area}")
    else:
        return(f"A area é {area} e o volume é {area*altura}")
