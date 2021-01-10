from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fastapi_jwt_auth.exceptions import AuthJWTException

# Project modules.
from app_api import router
from app_core.db import engine
from db_models import models_db
from app_core.config import SQLALCHEMY_DATABASE_URL

from fastapi_sqlalchemy import DBSessionMiddleware  
from fastapi_sqlalchemy import db  

from fastapi.middleware.cors import CORSMiddleware

#Create all models in db
models_db.Base.metadata.create_all(engine)

app = FastAPI(title='Moj Majstor')

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=SQLALCHEMY_DATABASE_URL)
app.include_router(router)

# Used in development
def recreate_database():
    models_db.Base.metadata.drop_all(engine)
    models_db.Base.metadata.create_all(engine)

