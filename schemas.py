from pydantic import BaseModel
from typing import Optional, List


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    admin: Optional[bool] = False

    class Config:
        from_attributes = True

class CompanyCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True

class ContractCreate(BaseModel):
    contract_number: str
    company_id: int

    class Config:
        from_attributes = True

class EmployeeCreate(BaseModel):
    name: str
    cpf: str
    position: str
    sector: str
    contract_id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True


class UserRead(BaseModel):
    id: int
    name: str
    email: str
    admin: bool

    class Config:
        from_attributes = True

class CompanyRead(CompanyCreate):
    id: int

    class Config:
        from_attributes = True

class EmployeeRead(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True

class ContractRead(ContractCreate):
    id: int

    class Config:
        from_attributes = True

class CompanyWithContracts(CompanyRead):
    contracts: List[ContractRead] = []

    class Config:
        from_attributes = True

class ContractWithEmployees(ContractRead):
    employees: List[EmployeeRead] = []

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    admin: Optional[bool] = None

    class Config:
        from_attributes = True