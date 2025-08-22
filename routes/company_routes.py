from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

companies_router = APIRouter(prefix="/companies", tags=["companies"])
