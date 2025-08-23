from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, create_engine
from sqlalchemy.orm import relationship, declarative_base

db = create_engine("sqlite:///database.db")
Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    contracts = relationship('Contract', back_populates='company')

class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    contract_number = Column(String, unique=True, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)


    company = relationship('Company', back_populates='contracts')
    employees = relationship('Employee', back_populates='contract')

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    position = Column(String)
    sector = Column(String)
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    contract = relationship('Contract', back_populates='employees')


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    admin = Column(Boolean, default=False)