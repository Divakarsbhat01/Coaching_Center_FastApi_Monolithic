in order to make this application work
Mongo DB
    create a database in mongo db with name users
    port: 27017
    create collection with name user_login
    data has to be in format:
        user_name:"ram@gmail.com"
        user_password: "$2b$12$kI4W/FRwZgLlhHECHict0OvbiagU8WKADnXLyezBzjbfMbu517BVm"
        user_role:"admin"
        user_id:1
    create collection with name user_id_counter
    data has to be in format:
        user_id_counter:6
        counter_name:"user_id_counter"
MysqlDB
    create a database in mysql db with name coachingcenter_fastapi_monolithic
    port: 3306

COmmands to run:
    python has to be installed in computer
    requirements in requirements.txt has to be installed
    uvicorn main:app --reload
    runs on port 8000
    
