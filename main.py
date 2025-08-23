from fastapi import FastAPI
from passlib.context import CryptContext

app = FastAPI()
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


from routes.auth_routes import auth_router
from routes.company_routes import companies_router
from routes.employee_routes import employees_router
from routes.contract_routes import contracts_router


app.include_router(auth_router)
app.include_router(companies_router)
app.include_router(employees_router)
app.include_router(contracts_router)
