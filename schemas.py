from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    admin: Optional[bool]

    class Config:
        from_attributes = True

class CompanySchema(BaseModel):
    name: str

    class Config:
        from_attributes = True

class ContractSchema(BaseModel):
    contract_number: str
    company_id: int

    class Config:
        from_attributes = True

class EmployeeSchema(BaseModel):
    name: str
    cpf: str
    position: str
    sector: str
    contract_id: int

    class Config:
        from_attributes = True