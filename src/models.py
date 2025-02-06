from sqlalchemy import Column, Integer, String, Float
from src.database import Base

class Product(Base):
    __tablename__ = "productos"
    
    product_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    store_id = Column(Integer, nullable=False)
