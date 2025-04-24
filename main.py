from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "MARHABA in Ghaymah"}

@app.get("/ping")
def ping():
    return {"status": "alive"}
