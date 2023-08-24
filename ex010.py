from fastapi import FastAPI

app=FastAPI()

@app.get("/suada/{nome}")

def top(nome):
    return(f"Tu {nome} es gay ")

@app.get("/area") #http://127.0.0.1:8000/area?largura=9&comprimento=9

def areatot(largura: int =2, comprimento: int =2):
    return(f"A area é {largura*comprimento}")

