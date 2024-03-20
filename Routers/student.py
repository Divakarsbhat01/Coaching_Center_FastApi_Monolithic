from fastapi import APIRouter,Depends,status,HTTPException
from Schemas import schemas
from Database import mysql_database_Config
from sqlalchemy.orm import Session 
from Models import models
from Security_and_Auth import authentication

router=APIRouter(tags=["student"])

@router.post("/create_student",status_code=status.HTTP_201_CREATED,response_model=schemas.Student_Response)
def create_student(new_student:schemas.New_Student,db:Session=Depends(mysql_database_Config.get_db),current_user:int=Depends(authentication.get_current_user)):
    student_to_be_added=models.Student(** new_student.dict())
    db.add(student_to_be_added)
    db.commit()
    db.refresh(student_to_be_added)
    return student_to_be_added

@router.get("/get_all_students")
def getting_all_students(db:Session=Depends(mysql_database_Config.get_db)
                         ,current_user:int=Depends(authentication.get_current_user)):
    data_to_send_back=db.query(models.Student).all()
    return data_to_send_back

@router.get("/get_student_by_id/{id}",response_model=schemas.Student_Response)
def getting_all_students(id:int,db:Session=Depends(mysql_database_Config.get_db),current_user:int=Depends(authentication.get_current_user)):
    data_to_send_back=db.query(models.Student).filter(models.Student.student_id==id).first()
    if data_to_send_back==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    return data_to_send_back

@router.delete("/delete_student_by_id/{id}",status_code=status.HTTP_200_OK)
def deleting_student(id:int,db:Session=Depends(mysql_database_Config.get_db),current_user:int=Depends(authentication.get_current_user)):
    x=db.query(models.Student).filter(models.Student.student_id==id)
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    x.delete(synchronize_session=False)
    db.commit()
    return {"Message":"Successful"}

@router.put("/update_student/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Student_Response)
def updating_student(id:int,update_student:schemas.Update_Student,db:Session=Depends(mysql_database_Config.get_db)
                     ,current_user:int=Depends(authentication.get_current_user)):
    x=db.query(models.Student).filter(models.Student.student_id==id)
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    x.update(update_student.dict())
    db.commit()
    send_back_to_user=db.query(models.Student).filter(models.Student.student_id==id).first()
    return send_back_to_user
    
               