from fastapi import FastAPI, Request
import ftpClient
import os
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/listFiles")
def listFiles():
    data = ftpClient.listFiles()
    return {"files": data}

@app.post("/store")
async def storeFile(item: Request):
    itemData = await item.json()
    print(itemData)
    ftpClient.uploadFile(itemData['file'])
    data = ftpClient.listFiles()
    return {"files": data}

@app.post("/retrieve")
async def retrieveFile(item: Request):
    itemData = await item.json()
    print(itemData)
    beforeFiles = os.listdir(os.curdir)
    ftpClient.downloadFile(itemData['file'])
    afterFiles = os.listdir(os.curdir)
    return {"beforeFiles": beforeFiles, "afterFiles": afterFiles}