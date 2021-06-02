from fastapi import FastAPI
from fastapi.params import Depends
from fastapi import FastAPI, HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import String
from starlette.responses import Response
from tasktodo import models, schemas
from tasktodo.hashing import Hash 
from tasktodo.database import SessionLocal, engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = models.User(first_name=request.first_name,last_name=request.last_name,user_name=request.user_name,
    email=request.email,status=request.status, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}',response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details = f"User with the id {id} is not found")
    return user

@app.get('/task/{id}', status_code=200, response_model=schemas.task)
def show(id:int, response: Response, db: Session = Depends(get_db)):
    task = db.query(models.User).filter(models.User.id==id).first()
    return task 