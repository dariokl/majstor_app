from fastapi import APIRouter, HTTPException, status, Body, Request
from typing import List

from fastapi_sqlalchemy import db

from pydantic_models.models_pydantic import Search, User, UserQuery
from db_models.models_db import User as UserDB
from db_models.models_db import Message


router = APIRouter()



@router.post('/', response_model=UserQuery)
def q_search(q: Search):

    query = UserQuery(users=db.session.query(UserDB).all())

    return query

@router.post('/q')
def new():

    new = Message(sender_id=1, recipient_id=2, body='Neka neka evo peka')
    db.session.add(new)
    db.session.commit()

    return 'a'