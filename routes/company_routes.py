from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Company, User
from schemas import CompanyRead, CompanyWithContracts, CompanyCreate
from dependencies import take_session, get_current_user, get_current_admin_user

companies_router = APIRouter(prefix="/companies", tags=["companies"])

@companies_router.get("/", response_model=List[CompanyRead])
async def get_companies(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user),
):
    companies = db.query(Company).offset(skip).limit(limit).all()
    return companies

@companies_router.get("/{company_id}", response_model=CompanyRead)
async def get_company(
        company_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user)
):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@companies_router.get("/{company_id}/details", response_model=CompanyWithContracts)
async def get_company_details(
        company_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user)
):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@companies_router.post("/", response_model=CompanyRead, status_code=201)
async def create_company(
        company: CompanyCreate,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_company = Company(name=company.name)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@companies_router.put("/{company_id}", response_model=CompanyRead)
async def update_company(
        company_id: int,
        company: CompanyCreate,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    db_company.name = company.name
    db.commit()
    db.refresh(db_company)
    return db_company

@companies_router.delete("/{company_id}", status_code=204)
async def delete_company(
        company_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    db.delete(db_company)
    db.commit()
    return