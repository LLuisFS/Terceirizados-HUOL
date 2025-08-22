from fastapi import FastAPI
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt

from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI()
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


from routes.auth_routes import auth_router
from routes.company_routes import companies_router
from routes.employee_routes import employees_router


app.include_router(auth_router)
app.include_router(companies_router)
app.include_router(employees_router)
