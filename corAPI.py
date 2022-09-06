# corAPI.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Corcom World"}


@app.get("/matrix1000")
async def displayMatrix():
    return {"message": "This is for matrix 1000 image"}

@app.put("/coradd")
async def addCoreComponent():
    return {"message": "This is for adding corecomponent"}