import os
from fastapi_jwt_auth import auth_jwt 
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT


basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'postgresql+psycopg2://{dariokl}:{lolpasspass12}@{localhost}:{majstor_db}'

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='dariok',pw='lolpasspass12',url='localhost:5432',db='majstor_db')

class Settings(BaseModel):
    authjwt_secret_key = 'secret'

@AuthJWT.load_config
def get_config():
    return Settings()
