from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, create_engine
from sqlalchemy.orm import relationship, declarative_base

db = create_engine("sqlite:///database.db")
Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Relação corrigida: aponta para o atributo 'company' na classe Contract
    contracts = relationship('Contract', back_populates='company')

class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    contract_number = Column(String, unique=True, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)

    # Relações corrigidas
    company = relationship('Company', back_populates='contracts')
    employees = relationship('Employee', back_populates='contract') # Aponta para 'contract' em Employee

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    position = Column(String)
    sector = Column(String)
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)

    # Relação corrigida: aponta para o atributo 'employees' em Contract
    contract = relationship('Contract', back_populates='employees')

# Não se esqueça de manter seu modelo User no arquivo também
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    admin = Column(Boolean, default=False)