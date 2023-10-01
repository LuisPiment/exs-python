from fastapi import FastAPI,Query
from typing import Union,List
from pydantic import BaseModel
app=FastAPI()

class Certificado(BaseModel):
    nome:str
    idade:int
    descrição:Union[str,int,None]=False
    morada:Union[str,int]

@app.get("/nomes")
def lista(nome:List[str]=Query(min_leght=4)):
    if len(nome)>5:
        return(f"Uau a sua lista é mt grande  {nome}")
    else:
        return(f"hmmmm a sua lista podia ser maior {nome}")


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
def bola(comprimento:int =Query(default=0,ge=0,le=100),largura:int=Query(default=0,ge=0,le=100),altura:int | None=False):
    area=comprimento*largura
    if altura==False:
        return(f"A area é {area}")
    else:
        return(f"A area é {area} e o volume é {area*altura}")
