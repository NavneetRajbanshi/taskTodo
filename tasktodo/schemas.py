from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean


class task(BaseModel):
    title: str
    body: str

class task(task):
    class Config():
        orm_mode = True


class User(BaseModel):
    first_name:str
    last_name: str
    user_name:str
    email:str
    password:str
    status:str

class ShowUser(BaseModel):
    first_name:str
    last_name: str
    user_name:str
    email:str
    
    class Config():
        orm_mode = True


