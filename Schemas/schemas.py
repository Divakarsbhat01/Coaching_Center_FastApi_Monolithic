from pydantic import BaseModel

class New_User(BaseModel):
    user_name:str
    user_password:str
    user_role:str

class User_Update(BaseModel):
    user_name:str
    user_password:str
    user_role:str

class Reset_Password(BaseModel):
    user_name:str
    user_password:str
    user_new_password:str

class User_Response(BaseModel):
    user_name:str
    user_id:int
    user_role:str

class User_Create_Response(BaseModel):
    user_name:str
    user_id:int
    user_role:str
    click_to_verify:str

class User_Login_Response(BaseModel):
    access_token:str
    type:str
    

class New_Student(BaseModel):
    first_name:str
    last_name:str	
    student_age:int	
    email_id:str

class Update_Student(BaseModel):
    first_name:str
    last_name:str	
    student_age:int	
    email_id:str

class Student_Response(BaseModel):
    first_name:str
    last_name:str	
    student_id:int
    student_age:int	
    email_id:str

class New_Parent(BaseModel):
    first_name:str	
    last_name:str		
    student_id:int
    email_id:str	

class Update_Parent(BaseModel):
    first_name:str	
    last_name:str		
    student_id:int	
    email_id:str	

class Parent_Response(BaseModel):
    first_name:str	
    last_name:str	
    student_id:int	
    student_id:int	
    email_id:str

class New_Course(BaseModel):
    course_name:str		
    course_desc:str	
    course_credit:int	

class Update_Course(BaseModel):
    course_name:str		
    course_desc:str	
    course_credit:int		

class Course_Response(BaseModel):
    course_name:str	
    course_id:int	
    course_desc:str	
    course_credit:int

class New_Course_Material(BaseModel):	
    course_id:int	
    course_material_url:str	

class Update_Course_Material(BaseModel):	
    course_material_url:str	

class Course_Material_Response(BaseModel):
    course_id:int	
    course_material_url:str		

class New_Teacher(BaseModel):
    teacher_first_name:str	
    teacher_last_name:str
    teacher_email:str	

class Update_Teacher(BaseModel):
    teacher_first_name:str	
    teacher_last_name:str
    teacher_email:str		

class Teacher_Response(BaseModel):
    teacher_first_name:str	
    teacher_id:int
    teacher_last_name:str
    teacher_email:str

class Student_Course(BaseModel):
    student_id:int	
    course_id:int

class Student_Course_response(BaseModel):
    student_id:int	
    course_id:int

class Teacher_Course(BaseModel):
    teacher_id:int	
    course_id:int

class Teacher_Course_response(BaseModel):
    teacher_id:int	
    course_id:int

    