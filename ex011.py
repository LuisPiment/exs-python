from fastapi import FastAPI
from pydantic import BaseModel
from random import randint
animal=[]
lista=[]
info=[]
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
    for c in lista:
        for a in c:
            print(a)
            print("-"*30)
            print(id1)
            print("*"*30)
            if a == id1:
                print("deu certo")
                info.append(lista[c][:])
                print(info)
            else:
                print("deu errado")
                print("*"*30)