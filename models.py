from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str |None
    address: str | None

class CustomerCreate(CustomerBase):
    id: int

