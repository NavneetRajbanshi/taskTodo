from fastapi import FastAPI
from tasktodo import models ,token , database, hashing , oauth2, schemas 
from tasktodo.database import engine
from  tasktodo.routers import task, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(task.router)
app.include_router(user.router)