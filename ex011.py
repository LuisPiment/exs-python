from fastapi import FastAPI
from pydantic import BaseModel
from random import randint
from Ferramentas import *
animal=[]
lista=[]

animais=FastAPI()

class Cadas(BaseModel):
    nome:str
    idade:int
    sexo:str
    cor:str

@animais.post("/animais")
def resposta(cadastro:Cadas):
    id=randint(1000,9999)
    animal.append(id)
    animal.append(cadastro.nome)
    animal.append(cadastro.idade)
    animal.append(cadastro.sexo)
    animal.append(cadastro.cor)
    lista.append(animal.copy())
    animal.clear()
    return(f"O animal {cadastro.nome}, com o {cadastro.idade} anos, do sexo {cadastro.sexo} e da cor {cadastro.cor} foi registrado com sucesso")

@animais.get("/animais")
def lista1():
    return(lista)

@animais.get("/animais/{id1}")
def animal2(id1):
    for v,c in enumerate(lista):
        if c[0] == int(id1):
           return(f"Os dados do seu animal sao os seguintes:"  
                  f"  Nome:{c[1]}"  
                  f"  Idade:{c[2]}"
                  f"  Sexo:{c[3]}"
                  f"  Cor:{c[4]}")
    

        if (len(lista)-1)==v:
            if c[0]!= int(id1):
                return(f"O id do seu animal n foi encontrado no sistema,Por favor tente novamente")
            

@animais.delete("/animais/{id1}")
def animal3(id1):
    for v,c in enumerate(lista):

        if c[0] == int(id1):
           lista.pop(v)
           return("Animal apagado do sistema com sucesso")
    

        if (len(lista)-1)==v:
            if c[0]!= int(id1):
                return(f"O id do seu animal n foi encontrado no sistema,Por favor tente novamente")
            S