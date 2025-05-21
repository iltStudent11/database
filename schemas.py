from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    Placed = "Placed"
    Shipped = "Shipped"
    Cancelled = "Cancelled"

class AddressBase(BaseModel):
    Street1: str
    Street2: Optional[str] = None
    City: str
    State: str
    Country: str
    ZIP: str

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    Id: int
    CustomerId: int
    class Config:
        orm_mode = True

class Product(BaseModel):
    Id: int
    Name: str
    Description: Optional[str]
    Price: int
    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    Name: str
    Email: EmailStr
    Phone: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    Id: int
    addresses: List[Address] = []
    class Config:
        orm_mode = True

class CustomerOrderBase(BaseModel):
    ProductId: int
    Quantity: int
    ShippingAddressId: int
    Status: OrderStatus

class CustomerOrderCreate(CustomerOrderBase):
    pass

class CustomerOrder(CustomerOrderBase):
    Id: int
    CustomerId: int
    CreationDte: datetime
    product: Optional[Product]
    class Config:
        orm_mode = True
