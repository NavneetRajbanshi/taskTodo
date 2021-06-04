from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean




class User(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: str
    password: str
    status: str
    super_user: str 

class ShowUser(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: str
    
    class Config():
        orm_mode = True



class Task(BaseModel):
    Task_Name: str
    Task_description: str

class ShowTask(BaseModel):
    Task_Name: str
    Task_description: str
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None