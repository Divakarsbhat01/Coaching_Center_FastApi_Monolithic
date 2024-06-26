from fastapi import APIRouter,Depends,status,HTTPException
from Schemas import schemas
from Database import mysql_database_Config
from sqlalchemy.orm import Session 
from Models import models
from Security_and_Auth import authentication

router=APIRouter(tags=["Course"])

@router.post("/create_course",status_code=status.HTTP_201_CREATED,response_model=schemas.Course_Response)
def create_course(new_course:schemas.New_Course,db:Session=Depends(mysql_database_Config.get_db)
                   ,current_user:int=Depends(authentication.get_current_user)):
    course_to_be_added=models.Course(** new_course.dict())
    db.add(course_to_be_added)
    db.commit()
    db.refresh(course_to_be_added)
    return course_to_be_added

@router.get("/get_all_courses")
def getting_all_courses(db:Session=Depends(mysql_database_Config.get_db),current_user:int=Depends(authentication.get_current_user)):
    data_to_send_back=db.query(models.Course).all()
    return data_to_send_back

@router.get("/get_Course_by_id/{id}",response_model=schemas.Course_Response)
def getting_the_Course(id:int,db:Session=Depends(mysql_database_Config.get_db),current_user:int=Depends(authentication.get_current_user)):
    data_to_send_back=db.query(models.Course).filter(models.Course.course_id==id).first()
    if data_to_send_back==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    return data_to_send_back

@router.delete("/delete_course_by_id/{id}",status_code=status.HTTP_200_OK)
def deleting_course(id:int,db:Session=Depends(mysql_database_Config.get_db),current_user:int=Depends(authentication.get_current_user)):
    x=db.query(models.Course).filter(models.Course.course_id==id)
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    x.delete(synchronize_session=False)
    db.commit()
    return {"Message":"Successful"}

@router.put("/update_course/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Course_Response)
def updating_course(id:int,update_course:schemas.Update_Course,db:Session=Depends(mysql_database_Config.get_db)
                     ,current_user:int=Depends(authentication.get_current_user)):
    x=db.query(models.Course).filter(models.Course.course_id==id)
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    x.update(update_course.dict())
    db.commit()
    send_back_to_user=db.query(models.Course).filter(models.Course.course_id==id).first()
    return send_back_to_user