from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import User
from schemas import UserRead, UserUpdate
from dependencies import take_session, get_current_user, get_current_admin_user

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@users_router.get("/", response_model=List[UserRead])
async def read_users(
        page: int = 1,
        size: int = 100,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    skip = (page - 1) * size
    db_users = db.query(User).offset(skip).limit(size).all()
    return db_users

@users_router.get("/{user_id}", response_model=UserRead)
async def read_user(
        user_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_user = db.query(User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@users_router.put("/{user_id}", response_model=UserRead)
async def update_user(
        user_id: int,
        user: UserUpdate,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_user = db.query(User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    return db_user

@users_router.delete("/{user_id}", status_code=204)
async def delete_user(
        user_id: int,
        db: Session = Depends(take_session),
        current_user: User = Depends(get_current_admin_user)
):
    db_user = db.query(User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return