from fastapi import FastAPI

app=FastAPI()

@app.get("/")

async def top():
    return("Foi um bom começo 22/08/2023")

