from fastapi import APIRouter, HTTPException, Query
from models import CustomerBase, CustomerCreate

customers: list[CustomerCreate] = []
next_id = 1

router = APIRouter(prefix="/customers", tags=["customers"]) 

@router.post("/")
async def create_customer(customer: CustomerBase) -> CustomerCreate:
    global next_id
    customer_out = CustomerCreate(id=next_id, **customer.model_dump())
    next_id += 1
    customers.append(customer_out)
    return customer_out

@router.get("/", response_model=list[CustomerCreate])
async def list_customers() -> list[CustomerCreate]:
    return customers

@router.delete("/{customer_id}")
async def delete_customer(customer_id: int):
    for i, customer in enumerate(customers):
        if customer.id == customer_id:
            deleted_customer = customers.pop(i)
            return {"message": f"Customer {deleted_customer.name} deleted successfully"}

@router.put("/{customer_id}", response_model=CustomerCreate)
async def update_customer(customer_id: int, customer: CustomerBase) -> CustomerCreate:
    for i, existing_customer in enumerate(customers):
        if existing_customer.id == customer_id:
            updated_customer = CustomerCreate(id=customer_id, **customer.model_dump())
            customers[i] = updated_customer
            return updated_customer