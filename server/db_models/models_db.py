from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.util.deprecations import deprecated
from sqlalchemy import Column, String, Integer, TEXT, JSON, DateTime

from datetime import datetime

from fastapi_sqlalchemy import db

from app_core.db import Base

from passlib.context import CryptContext

# Define the encryption schema for passlib !
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    company_name = Column(String, unique=True)
    entity = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    portfolio = Column(Boolean, default=False)
    info = Column(JSON, nullable=False, default=dict, server_default='{}')
    profile_completed = Column(Integer, default=0)

    projects = relationship('Portfolio', backref='projects')
    inbox = relationship('Message', foreign_keys='Message.recipient_id', \
     backref='recipient', lazy='dynamic')

    outbox = relationship('Message', foreign_keys='Message.sender_id', \
        backref='author', lazy='dynamic')
    
    last_read = Column(DateTime)
    message_counter = Column(Integer)
    

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError("Password is not readable attribute")

    @password.setter
    def password(self, password):
        self.hashed_password = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)
    
    def new_messages(self):
        last_read_time = self.last_read or datetime(1900, 1 , 1)
        count = db.session.query(Message) \
            .filter_by(recipient_id=self.id).filter(Message.timestamp > last_read_time).count()
        self.message_counter = count
        db.session.commit()
        db.session.close()

    def verification(self):
        part = 0
        whole = 6

        if self.city:
            part += 1

        if self.address:
            part += 1

        if self.info.get('phone'):
            part += 1

        if self.info.get('about'):
            part += 1

        if self.portfolio == True:
            part += 1

        if self.info.get('title'):
            part += 1

        self.profile_completed = 100 * float(part)/float(whole)
        db.session.commit()

        return self.profile_completed


class Message(Base):

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    recipient_id = Column(Integer, ForeignKey('users.id'))
    body = Column(String(140))
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)

class Portfolio(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    link = Column(String)
    description = Column(TEXT)

    user_id = Column(Integer, ForeignKey('users.id'))
