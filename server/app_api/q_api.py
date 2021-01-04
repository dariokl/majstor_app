from fastapi import APIRouter, HTTPException, status, Body, Request

from fastapi_sqlalchemy import db

router = APIRouter()


@router.post('/')
def q_search(q):

    if q:

        return {'message': 'ok'}
    
    else:
        return {'message': 'no'}