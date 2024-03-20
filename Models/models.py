from Database.mysql_database_Config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Student(Base):
    __tablename__="Student"
    first_name=Column(String(50),nullable=False)
    last_name=Column(String(50),nullable=False)
    student_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    student_age=Column(Integer,nullable=False)
    email_id=Column(String(100),nullable=False)


class Mentor(Base):
    __tablename__="Parent"
    first_name=Column(String(50),nullable=False)
    last_name=Column(String(50),nullable=False)
    parent_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    student_id=Column(Integer,ForeignKey("Student.student_id",ondelete="CASCADE"),nullable=False)
    email_id=Column(String(100),nullable=False)

class Course(Base):
    __tablename__="Course"
    course_name=Column(String(50),nullable=False,unique=True)
    course_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    course_desc=Column(String(100),nullable=False)
    course_credit=Column(Integer,nullable=False)

class Teacher(Base):
    __tablename__="Teacher"
    teacher_first_name=Column(String(50),nullable=False)
    teacher_last_name=Column(String(50),nullable=False)
    teacher_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    teacher_email=Column(String(50),nullable=False)

class course_material(Base):
    __tablename__="Course_Material"
    course_material_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    course_material_url=Column(String(100),nullable=False)
    course_id=course_id=Column(Integer,ForeignKey("Course.course_id",ondelete="CASCADE"),nullable=False)

class Student_Course(Base):
    __tablename__="Student_Course"
    table_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    student_id=Column(Integer,ForeignKey("Student.student_id",ondelete="CASCADE"),nullable=False)
    course_id=Column(Integer,ForeignKey("Course.course_id",ondelete="CASCADE"),nullable=False)

class Teacher_Course(Base):
    __tablename__="Teacher_Course"
    table_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    teacher_id=Column(Integer,ForeignKey("Teacher.teacher_id",ondelete="CASCADE"),nullable=False)
    course_id=Column(Integer,ForeignKey("Course.course_id",ondelete="CASCADE"),nullable=False)



