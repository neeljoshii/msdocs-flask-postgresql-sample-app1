from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import validates

from app import db


class Product(db.Model):
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Float)

    def __str__(self):
        return self.name
