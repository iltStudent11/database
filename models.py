from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class OrderStatus(enum.Enum):
    Placed = "Placed"
    Shipped = "Shipped"
    Cancelled = "Cancelled"

class Customer(Base):
    __tablename__ = 'Customer'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255), nullable=False)
    Email = Column(String(255), nullable=False)
    Phone = Column(String(50))
    addresses = relationship("Address", back_populates="customer")
    orders = relationship("CustomerOrder", back_populates="customer")

class Address(Base):
    __tablename__ = 'Address'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    CustomerId = Column(Integer, ForeignKey('Customer.Id'), nullable=False)
    Street1 = Column(String(255), nullable=False)
    Street2 = Column(String(255))
    City = Column(String(100), nullable=False)
    State = Column(String(100), nullable=False)
    Country = Column(String(100), nullable=False)
    ZIP = Column(String(20), nullable=False)
    customer = relationship("Customer", back_populates="addresses")

class Product(Base):
    __tablename__ = 'Product'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255), nullable=False)
    Description = Column(Text)
    Price = Column(Integer, nullable=False)

class CustomerOrder(Base):
    __tablename__ = 'CustomerOrder'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    CustomerId = Column(Integer, ForeignKey('Customer.Id'), nullable=False)
    ProductId = Column(Integer, ForeignKey('Product.Id'), nullable=False)
    Quantity = Column(Integer, nullable=False)
    ShippingAddressId = Column(Integer, ForeignKey('Address.Id'), nullable=False)
    CreationDte = Column(DateTime, nullable=False)
    Status = Column(Enum(OrderStatus), nullable=False)
    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product")
    shipping_address = relationship("Address")
