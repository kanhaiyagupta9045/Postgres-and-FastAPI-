from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from database import Base

class Bank(Base):
    __tablename__ = "banks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(49), unique=True, index=True, nullable=False)
    branches = relationship("Branch", back_populates="bank", cascade="all, delete-orphan")

class Branch(Base):
    __tablename__ = "branches"

    ifsc = Column(String(11), primary_key=True, index=True)
    bank_id = Column(Integer, ForeignKey("banks.id"))
    branch = Column(String(74), nullable=False)
    address = Column(String(195), nullable=False)
    city = Column(String(50), nullable=False)
    district = Column(String(50), nullable=False)
    state = Column(String(26), nullable=False)

    bank = relationship("Bank", back_populates="branches")
