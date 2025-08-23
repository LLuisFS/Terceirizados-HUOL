from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import User, Contract
from schemas import ContractRead, ContractWithEmployees, ContractCreate
from dependencies import take_session, get_current_user, get_current_admin_user


contracts_router = APIRouter(prefix="/contracts", tags=["contracts"])

@contracts_router.get("/", response_model=List[ContractRead])
async def get_contracts(
        page: int = 1,
        size: int = 100,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user)
):
    skip = (page - 1) * size
    companies = db.query(Contract).offset(skip).limit(size).all()
    return companies

@contracts_router.get("/{contract_id}", response_model=ContractRead)
async def get_contract(
        contract_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user)
):
    company = db.query(Contract).get(contract_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Contract not found")
    return company

@contracts_router.get("/{contract_id}/details", response_model=ContractWithEmployees)
async def get_contract_details(
        contract_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user)
):
    db_contract = db.query(Contract).get(contract_id).first()
    if not db_contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    return db_contract

@contracts_router.post("/", response_model=ContractRead, status_code=201)
async def create_contract(
        contract: ContractCreate,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_contract = Contract(contract_number=contract.contract_number, company_id=contract.company_id)
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

@contracts_router.put("/{contract_id}", response_model=ContractRead)
async def update_contract(
        contract_id: int,
        contract: ContractCreate,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if db_contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")
    db_contract.contract_number = contract.contract_number
    db_contract.company_id = contract.company_id
    db.commit()
    db.refresh(db_contract)
    return db_contract

@contracts_router.delete("/{contract_id}", status_code=204)
async def delete_contract(
        contract_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if db_contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")
    db.delete(db_contract)
    db.commit()
    return