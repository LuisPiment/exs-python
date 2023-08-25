from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

@app.get("/usuario/{nome}")

def top(nome):
    return(f"{'Tu es gay                               '*400}0")

@app.get("/area") #http://127.0.0.1:8000/area?largura=9&comprimento=9

def areatot(largura: int =2, comprimento: int =2):
    return(f"A area é {largura*comprimento}")

class Loja(BaseModel):
    nome:str
    valor:float
    dia:int

@app.post("/produtos")
def lojinha(lojota:Loja):
    return(f"O produto {lojota.nome} com o preço {lojota.valor} no dia {lojota.dia}, foi registrado com sucesso")

