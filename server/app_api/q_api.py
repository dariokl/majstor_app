from fastapi import APIRouter, HTTPException, status, Body, Request
from typing import List

from fastapi_sqlalchemy import db

from pydantic_models.models_pydantic import Search, User, UserQuery
from db_models.models_db import User as UserDB

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

router = APIRouter()
PydanticModel = sqlalchemy_to_pydantic(UserDB)

class Py(PydanticModel):
    mom = List[PydanticModel] = []

@router.post('/')
def q_search(q: Search):

    query = db.session.query(UserDB).all()

    PydanticModel = sqlalchemy_to_pydantic(UserDB)

    query_u = Py.from_orm(query)

    query_py = query_u.dict()
    return query_py


