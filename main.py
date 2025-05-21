import os
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, Customer, Address, Product, CustomerOrder, OrderStatus
from schemas import Customer as CustomerSchema, Address as AddressSchema, Product as ProductSchema, CustomerOrder as CustomerOrderSchema, AddressCreate, CustomerOrderCreate
from typing import List
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/customers/{customer_id}", response_model=CustomerSchema)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.Id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.get("/customers", response_model=List[CustomerSchema])
def get_all_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@app.get("/customers/{customer_id}/addresses", response_model=List[AddressSchema])
def get_addresses_for_customer(customer_id: int, db: Session = Depends(get_db)):
    addresses = db.query(Address).filter(Address.CustomerId == customer_id).all()
    return addresses

@app.get("/customers/{customer_id}/orders", response_model=List[CustomerOrderSchema])
def get_orders_for_customer(customer_id: int, db: Session = Depends(get_db)):
    orders = db.query(CustomerOrder).filter(CustomerOrder.CustomerId == customer_id).all()
    return orders

@app.post("/customers/{customer_id}/addresses", response_model=AddressSchema)
def add_address_for_customer(customer_id: int, address: AddressCreate, db: Session = Depends(get_db)):
    db_address = Address(**address.model_dump(), CustomerId=customer_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

@app.post("/customers/{customer_id}/orders", response_model=CustomerOrderSchema)
def add_order_for_customer(customer_id: int, order: CustomerOrderCreate, db: Session = Depends(get_db)):
    db_order = CustomerOrder(**order.model_dump(), CustomerId=customer_id, CreationDte=datetime.now(timezone.utc))
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
