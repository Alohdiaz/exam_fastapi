from fastapi import FastAPI
from models import CustomerBase, CustomerCreate

app = FastAPI()

customers: list[CustomerCreate] = []
next_id = 1

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/customers/")
async def create_customer(customer: CustomerBase) -> CustomerCreate:
    global next_id
    customer_out = CustomerCreate(id=next_id, **customer.model_dump())
    next_id += 1
    customers.append(customer_out)
    return customer_out
@app.get("/list_customers/", response_model=list[CustomerCreate])
async def list_customers() -> list[CustomerCreate]:
    return customers