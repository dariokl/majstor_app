from pydantic import BaseModel, EmailStr
from typing import Optional, List
from sqlalchemy.sql.sqltypes import Boolean


class User(BaseModel):
    """
    Base model class used later on for various puropuses , editing , using hash method etc...
    """
    name: str 
    last_name: str
    company_name: str
    entity: str
    city: str
    address: str
    email: EmailStr
    info: Optional[dict]
    portfolio: bool
    profile_completed: Optional[int]

    class Config:
        orm_mode = True





class UserIn(User):
    """
    Check the models_db.py to understand the hashing method.
    """
    hashed_password: str

class Portfolio(BaseModel):
    """
    Single portfolio item defined to contain name , description and link from the Portfolio database model.
    """
    id: int
    name: str
    description: str
    link: str

    class Config:
        orm_mode = True

class DeletePortfolio(BaseModel):
    id: int

    
class UserInfo(User):
    """
    One user can have up to 3 portfolios so this model contain list of model Portfolio.
    """
    projects: List[Portfolio]

    class Config:
        orm_mode = True

class UserList(BaseModel):
    name: str
    last_name: str
    company_name: str
    entity: str
    address: str
    email: EmailStr
    info: Optional[dict]
    projects: List[Portfolio]

    class Config:
        orm_mode = True

class UserQuery(BaseModel):
    users: List[UserList] = []

    class Config:
        orm_mode = True


class UserEidit(BaseModel):
    """
    Model used to edit informations for existing users.
    """
    name: str 
    last_name: str
    entity: str
    city: str
    address: str
    info: Optional[dict]

class LoginUser(BaseModel):
    email: EmailStr
    password: str

class Search(BaseModel):
    q : str
