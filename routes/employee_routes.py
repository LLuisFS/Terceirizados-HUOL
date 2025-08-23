from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import User, Employee
from schemas import EmployeeRead, EmployeeCreate
from dependencies import  take_session, get_current_user, get_current_admin_user


employees_router = APIRouter(prefix="/employees", tags=["employees"])


@employees_router.get("/", response_model=List[EmployeeRead])
async def get_employees(
        page: int = 1,
        size: int = 100,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user)
):
    skip = (page - 1) * size
    db_employees = db.query(Employee).offset(skip).limit(size).all()
    return db_employees

@employees_router.get("/{employee_id}", response_model=EmployeeRead)
async def get_employee(
        employee_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_user)
):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@employees_router.post("/", response_model=EmployeeRead)
async def create_employee(
        employee: EmployeeCreate,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_employee = Employee(name=employee.name, cpf=employee.cpf, position=employee.position, sector=employee.sector, contract_id=employee.contract_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@employees_router.put("/{employee_id}", response_model=EmployeeRead)
async def update_employee(
        employee_id: int,
        employee: EmployeeCreate,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    update_data = employee.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@employees_router.delete("/{employee_id}", status_code=204)
async def delete_employee(
        employee_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return
