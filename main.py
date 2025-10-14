from fastapi import FastAPI
from models import Customer

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/customers/")
async def create_customer(customer: Customer):
    return customer