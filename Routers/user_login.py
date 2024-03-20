import collections
from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Schemas import schemas
from Database import mongo_database_Config as mongodb
from fastapi import HTTPException,status
from Security_and_Auth import authentication,pass_hash

router=APIRouter(tags=["user_login"])

@router.post("/create_user",status_code=status.HTTP_200_OK,response_model=schemas.User_Create_Response)
def user_create(new_user:schemas.New_User):
    x=mongodb.user_id_counter_var.find()
    y=x[0]
    incremented_value=y["user_id_counter"]+1
    insert_prep=new_user.dict()
    insert_prep.update({"user_id":incremented_value})
    insert_prep["user_password"]=pass_hash.hash_the_password(insert_prep["user_password"])
    click_to_verify_link=f"http://localhost:8000/verify_user_creation/?user_id={incremented_value}"
    insert_prep.update({"click_to_verify":click_to_verify_link })
    mongodb.user_login_var.insert_one(insert_prep)
    mongodb.user_id_counter_var.update_one({"counter_name": "user_id_counter"},{ "$set": { "user_id_counter":incremented_value } } )
    return insert_prep

@router.post("/login",status_code=status.HTTP_202_ACCEPTED,response_model=schemas.User_Login_Response)
def user_login(user_cred:OAuth2PasswordRequestForm=Depends()):
    x=mongodb.user_login_var.find_one({"user_name":user_cred.username})
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid user credentials")
    db_user_id=x["user_id"]
    db_user_password=x["user_password"]
    if pass_hash.verify_the_password(user_cred.password,db_user_password)==False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid user credentials of password")
    access_token=authentication.create_access_token(data={"user_id":db_user_id})
    return {"access_token":access_token,"type":"Bearer"}

@router.put("/user_update/{auser_id}",status_code=status.HTTP_200_OK,response_model=schemas.User_Response)
def user_update(user_update:schemas.User_Update,auser_id:int):
    mongodb.user_login_var.update_one({"user_id":auser_id},{"$set":{"user_name":user_update.user_name,
                                                                    "user_password":user_update.user_password,
                                                                    "user_role":user_update.user_role}})
    return_prep=user_update.dict()
    return_prep.update({"user_id":auser_id})
    return return_prep

@router.delete("/user_delete/{auser_id}",status_code=status.HTTP_200_OK)
def user_delete(auser_id:int):
    x=mongodb.user_login_var.find_one({"user_id":auser_id})
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Dosen't exist")
        return{"Message":"Failed, user dosen't exist"}
    mongodb.user_login_var.delete_one({"user_id":auser_id})
    return {"Message":"Successful"}

@router.get("/verify_user_creation/",status_code=status.HTTP_202_ACCEPTED)
async def user_verify(user_id:int=0):
    return {"User Successfully verified":user_id}

@router.post("/resetpassword/{auser_id}",status_code=status.HTTP_200_OK)
async def user_password_reset(auser_id:int,new_pass:schemas.Reset_Password):
    x=mongodb.user_login_var.find_one({"user_id":auser_id})
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Dosen't exist")
        return{"Message":"Failed, user dosen't exist"}
    mongodb.user_login_var.update_one({"user_id":auser_id},{"$set":{"user_name":new_pass.user_name,
                                                                    "user_password":pass_hash.hash_the_password(new_pass.user_new_password)
                                                                    }})
    return {"Message":"User password successfully reset"}

    
