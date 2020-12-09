from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.util.deprecations import deprecated
from sqlalchemy import Column, String, Integer, TEXT, JSON

from app_core.db import Base

from passlib.context import CryptContext

#Define the encryption schema for passlib !
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer , primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    company_name = Column(String)
    entity = Column(String)
    city = Column(String)
    address = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    portfolio = Column(Boolean, default=False)
    info = Column(JSON, nullable=False, default=dict, server_default='{}')

    projects = relationship('Portfolio', backref='projects')

    @property
    def password(self):
        raise AttributeError("Password is not readable attribute")

    @password.setter
    def password(self, password):
        self.hashed_password = pwd_context.hash(password)
    
    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)
    
        


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(TEXT)


class Portfolio(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    link = Column(String)
    description = Column(TEXT)

    user_id = Column(Integer, ForeignKey('users.id'))




