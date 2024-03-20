import json
import logging
from fastapi import FastAPI
from httpx import AsyncClient
import httpx
from Configuration.config import settings
from Routers import abc_queries, course_material,course,mentor,student,teacher,user_login
from Database import mongo_database_Config as mongodb
from Models import models
from Database.mysql_database_Config import engine

app = FastAPI()
app.include_router(abc_queries.router)
app.include_router(course_material.router)
app.include_router(course.router)
app.include_router(mentor.router)
app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(user_login.router)

client = AsyncClient()

logging.getLogger('passlib').setLevel(logging.ERROR)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def api_working_status():
    return {"Status": settings.upstatus}



    


