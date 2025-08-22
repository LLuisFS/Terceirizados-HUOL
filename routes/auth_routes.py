from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas import UserCreate, UserRead, Token
from models import User
from dependencies import take_session
from main import bcrypt_context, create_token

auth_router = APIRouter(prefix="/auth", tags=["auth"])


def authenticate_user(email: str, password: str, session: Session):
    user = session.query(User).filter(User.email == email).first()
    if not user or not bcrypt_context.verify(password, user.password):
        return None
    return user


@auth_router.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(take_session)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")

    hashed_password = bcrypt_context.hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        admin=user.admin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@auth_router.post("/login", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(take_session),
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}