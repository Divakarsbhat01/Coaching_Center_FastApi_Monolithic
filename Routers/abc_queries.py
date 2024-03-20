from fastapi import APIRouter, Depends
from Schemas import schemas
from Database import mysql_database_Config
from sqlalchemy.orm import Session 
from Models import models
from Security_and_Auth import authentication
from sqlalchemy import func

router=APIRouter(tags=["abc_queries"])

@router.post("/student/course",response_model=schemas.Student_Course_response)
def student_course(new_student_course:schemas.Student_Course,db:Session=Depends(mysql_database_Config.get_db)
                   ,current_user:int=Depends(authentication.get_current_user)):
    student_course_to_be_added=models.Student_Course(** new_student_course.dict())
    db.add(student_course_to_be_added)
    db.commit()
    db.refresh(student_course_to_be_added)
    return student_course_to_be_added

@router.post("/teacher/course",response_model=schemas.Teacher_Course_response)
def student_course(new_teacher_course:schemas.Teacher_Course,db:Session=Depends(mysql_database_Config.get_db)
                   ,current_user:int=Depends(authentication.get_current_user)):
    teacher_course_to_be_added=models.Teacher_Course(** new_teacher_course.dict())
    db.add(teacher_course_to_be_added)
    db.commit()
    db.refresh(teacher_course_to_be_added)
    return teacher_course_to_be_added

@router.get("/studentsmentors")
def students_and_their_respective_mentors(db:Session=Depends(mysql_database_Config.get_db)
                                          ,current_user:int=Depends(authentication.get_current_user)):
    reasults=db.query(models.Student.student_id,
                      models.Student.first_name
                      ,models.Student.last_name
                      ,models.Mentor.parent_id
                      ,models.Mentor.first_name
                      ,models.Mentor.last_name).join(models.Mentor,models.Student.student_id==models.Mentor.student_id).all()
    ret_list=[]
    for i in reasults:
        ret_dict={}
        ret_dict.update({"Student_id":i[0]
                         ,"student_first_name":i[1]
                         ,"student_last_name":i[2]
                         ,"parent_id":i[3]
                         ,"parent_first_name":i[4]
                         ,"parent_last_name":i[5]
                         })
        ret_list.append(ret_dict)
    return ret_list

@router.get("/student_count")
def count_the_students(db:Session=Depends(mysql_database_Config.get_db)
                       ,current_user:int=Depends(authentication.get_current_user)):
    reasult=db.query(models.Student).count()
    return {"No_of_students":reasult}

@router.get("/course_count")
def count_the_students(db:Session=Depends(mysql_database_Config.get_db)
                       ,current_user:int=Depends(authentication.get_current_user)):
    reasult=db.query(models.Course).count()
    return {"No_of_Courses":reasult}

@router.get("/course_with_material")
def courses_with_their_materials(db:Session=Depends(mysql_database_Config.get_db)
                                ,current_user:int=Depends(authentication.get_current_user)):
    ret_list=[]
    reasult=db.query(models.Course.course_id
                     ,models.Course.course_name
                     ,models.course_material.course_material_id
                     ,models.course_material.course_material_url).join(models.course_material,models.Course.course_id==models.course_material.course_material_id).all()
    for i in reasult:
        ret_dict={}
        ret_dict.update({
                        "course_id":i[0],
                         "course_name":i[1],
                         "course_material_id":i[2],
                         "Course_material_url":i[3]
                         })
        ret_list.append(ret_dict)
    return ret_list

@router.get("/student_with_course")
def student_with_their_course(db:Session=Depends(mysql_database_Config.get_db)
                            ,current_user:int=Depends(authentication.get_current_user)):
    student_res=db.query(models.Student.first_name,models.Student.last_name,models.Student.student_id).all()
    course_res=db.query(models.Student_Course.course_id,
                        models.Student_Course.student_id
                        ,models.Course.course_name,
                        models.Course.course_credit).join(models.Course,models.Student_Course.course_id==models.Course.course_id).all()
    print(student_res,"\n\n",course_res)
    ret_list=[]
    for i in student_res:
        for j in course_res:
            ret_dict={}
            if i[2]==j[1]:
                ret_dict.update({"Student_first_name":i[0],
                                 "Student_last_name":i[1],
                                 "STudent_id":i[2],
                                 "COurse_name":j[0],
                                 "Course_credit":j[2]})
                ret_list.append(ret_dict)
    return ret_list

@router.get("/courses_student_count")
def courses_with_their_student_count(db:Session=Depends(mysql_database_Config.get_db)
                                     ,current_user:int=Depends(authentication.get_current_user)):
    reasults_partial=db.query(models.Course.course_name
                      ,models.Student_Course.course_id
                      ,func.count(models.Student_Course.student_id))
    reasults=reasults_partial.join(models.Course,models.Student_Course.course_id==models.Course.course_id).group_by(models.Student_Course.course_id).all()
    ret_list=[]
    ret_dict=[]
    for i in reasults:
        ret_dict={}
        ret_dict.update({"Course_name":i[0],"Course_id":i[1],"STudent_count":i[2]})
        ret_list.append(ret_dict)
    return ret_list

@router.get("/courses_teacher_count")
def courses_with_their_student_count(db:Session=Depends(mysql_database_Config.get_db)
                                     ,current_user:int=Depends(authentication.get_current_user)):
    reasults_partial=db.query(models.Course.course_name
                      ,models.Teacher_Course.course_id
                      ,func.count(models.Teacher_Course.teacher_id))
    reasults=reasults_partial.join(models.Course,models.Teacher_Course.course_id==models.Course.course_id).group_by(models.Teacher_Course.course_id).all()
    print(reasults)
    ret_list=[]
    ret_dict=[]
    for i in reasults:
        ret_dict={}
        ret_dict.update({"Course_name":i[0],"Course_id":i[1],"Teacher_count":i[2]})
        ret_list.append(ret_dict)
    return ret_list


