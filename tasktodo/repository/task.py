from sqlalchemy.orm import Session
from tasktodo import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    task = db.query(models.Task).all()
    return task

def create(request: schemas.Task, db: Session):
    new_task = models.Task(Task_Name=request.Task_Name, Task_description=request.Task_description, user_id=1)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def destroy(id:int, db: Session):
    task = db.query(models.Task).filter(models.Task.id == id)

    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'{"Task with id {id} not found"}')

    task.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Task, db:Session):
    task = db.query(models.Task).filter(models.Task.id == id)

    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {id} not found")

    task.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with the id {id} is not available")
    return task