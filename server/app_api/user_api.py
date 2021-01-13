from pathlib import Path
import shutil

from fastapi import APIRouter, Depends, HTTPException, status, Body, File, UploadFile, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT

from db_models.models_db import User as UserDB
from db_models.models_db import Portfolio as PortfolioDB

from pydantic_models.models_pydantic import User, UserIn, LoginUser, UserEidit, UserInfo, DeletePortfolio

from datetime import datetime, timedelta
from typing import Optional, Union, Dict, Any

from sqlalchemy.orm import contains_eager, subqueryload
from fastapi_sqlalchemy import db  

router = APIRouter()

@router.post('/login')
def login(user: LoginUser, Authorize: AuthJWT = Depends()):
    """
    Login view with fast_api-jwt-auth , returns access_token that is stored on client side and used to authorize user.
    """
    _user = db.session.query(UserDB).filter(UserDB.email==user.email).first()

    if _user != None and _user.verify_password(user.password):
            access_token = Authorize.create_access_token(subject=_user.id)

            return {"access_token" : access_token}
    else:
        raise HTTPException(status_code=401, detail="Bad username or password")


@router.get('/user', response_model=UserInfo, status_code=200)
def user(Authorize: AuthJWT = Depends()):
    """
    Authorize using fastapi_jwt_auth taking the id of user to query db and provide data to front end
    """
    Authorize.jwt_required()
    currentuser_id = Authorize.get_jwt_subject()
    user = db.session.query(UserDB).filter(UserDB.id==currentuser_id).first()
    user.verification()
    user.new_messages()
    user_response = db.session.query(UserDB).options(subqueryload(UserDB.projects)).filter(UserDB.id==currentuser_id).first()
    
    return user_response


@router.post('/register', status_code=200)
async def register(user: UserIn):
    """
    Registration router taking the query parameters from UserIn pydantic model with password field to be provided
    """

    email_check = 'a'

    if email_check == 1:
        return HTTPException(status_code=422, detail={'message': 'Email je vec u upotrebi'})
    else:
        new_user = UserDB(name=user.name, last_name=user.last_name, password=user.hashed_password, company_name=user.company_name, \
        entity=user.entity, city=user.city, address=user.address, email=user.email)
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user) 
        return JSONResponse(status_code=200, content={'message': 'Uspjesno ste izvrsili registraciju'})

@router.put('/edit', response_model=User)
def edit_profile(edit: UserEidit = Body(...), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    currentuser_id = Authorize.get_jwt_subject()
    user = db.session.query(UserDB).filter_by(id=currentuser_id).first()
    user.entity = edit.entity
    user.info = edit.info
    if user.profile_completed == 100:
        pass
    else:
        user.verification()
    db.session.commit()
    db.session.refresh(user)

    return user

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    currentuser_id= Authorize.get_jwt_subject()

    user = db.session.query(UserDB).filter(UserDB.id==currentuser_id).first()

    
    container = Path('/home/dariok/Desktop/flask_apps/moj_majstor_f/front_end/src/assets/img')


    if container.joinpath('{}'.format(user.email)).is_dir():
        user_dir = container.joinpath('{}'.format(user.email))
        #dir = Path.mkdir(user_dir)
        with open(user_dir.joinpath(file.filename), 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
            if len(user.projects) == 3:
                raise HTTPException(status_code=403, detail='Dostigli ste maksimalan broj mogucih objava !')
            
            else:
                new = PortfolioDB(name='test1', description='test1', link=str(user_dir.joinpath(file.filename)), user_id=currentuser_id)
                db.session.add(new)
                db.session.commit()
                if user.portfolio == False:
                    user.portfolio = True
                    db.session.commit()
                    db.session.close()

    else:
        user_dir = container.joinpath('{}'.format(user.email))
        dir = Path.mkdir(user_dir)

        return {dir}
        
    return {"a" : 's'}


@router.delete('/delete-post')
def delete_post(id : DeletePortfolio, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required
    current_user = Authorize.get_jwt_subject()

    post = db.session.query(PortfolioDB).filter_by(id = id.id).first()

    user = db.session.query(UserDB).filter_by(id = current_user).first()

    if post:
        db.session.delete(post)
        db.session.commit()
        if len(user.projects) == 0:
            user.portfolio = False
            db.session.commit()
            db.session.close()
        
        
    return id


@router.get('/checkperc')
def check_perc():

    user = db.session.query(UserDB).first()

    a = user.verification()


    return a




