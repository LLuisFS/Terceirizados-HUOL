from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Employee
from schemas import EmployeeRead
from dependencies import  take_session


employees_router = APIRouter(prefix="/employees", tags=["employees"])

@employees_router.get("/{employee_id}", response_model=EmployeeRead)
async def get_employee(employee_id: int, session: Session = Depends(take_session)):
    db_employee = session.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


