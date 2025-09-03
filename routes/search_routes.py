from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List
from models import User, Company, Contract, Employee
from schemas import MultiSearchResponse
from dependencies import take_session, get_current_user

search_router = APIRouter(prefix="/search", tags=["search"])

@search_router.get("/", response_model=List[MultiSearchResponse])
async def multi_entity_search(
        q: str = Query(..., min_lenght=3, description="Termo de busca com no mínimo 3 caracteres"),
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user)
):
    search_term = f"{q.lower()}%"
    found_companies = db.query(Company).filter(Company.name.ilike(search_term)).all()
    found_contracts = db.query(Contract).filter(Contract.contract_number.ilike(search_term)).all()
    found_employees = db.query(Employee).filter(
            or_(
                Employee.name.ilike(search_term),
                Employee.position.ilike(search_term),
                Employee.sector.ilike(search_term)
            )).all()

    return {
        "companies": found_companies,
        "contracts": found_contracts,
        "employees": found_employees,
    }
