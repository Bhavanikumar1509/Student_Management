""" This is Employee Management System . In  which 
we can perform crud operations on employee details. """

from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from datetime import datetime
from auth.jwt_handler import signJWT

client = MongoClient('mongodb://172.17.0.2:27017/')
'''docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name> 
to find the  mongo db container ipaddress
'''
db = client['mydatabase']
collection = db['myEmployee']
app = FastAPI()
class Employee(BaseModel):
    name:str
    empid: int 
    password:str
    empSalary: float
    Department: str
    Date_of_joining: datetime
    class cofig:
        the_schema={
            "user_demo":{
                "name":"beck",
                "empid":123,
                "empSalary":223.66,
                "Department":"java",
                "Date_of_joining":"2021-05-12T06:11:38.268000"
            }
        }
           
#create an employee
@app.post("/addEmployee" )
async def create_employee(employee:Employee):
    """this is the method useing for creating the employee"""
    user_data=employee.dict()
    res=collection.insert_one(user_data)
    return {"message":"user added sucessfully with ","_id": str(res.inserted_id)}


#get All Employee
@app.get("/getEmployees")
async def get_employees():
    data=[]
    for doc in collection.find():
        doc['_id']=str(doc['_id'])
        data.append(doc)
    return data

#get employee by id
@app.get("/getbyId")
async def get_by_id(empid:int):
    emp=[]
    k=collection.find({"empid":empid})
    for doc in k:
        doc['_id'] = str(doc['_id'])
        emp.append(doc)
    return emp

# get employee by department
@app.get("/getbydepartment")
async def get_by_department(department:str):
    emp=[]
    k=collection.find({"Department":department})
    for doc in k:
        doc['_id']=str(doc['_id'])
        emp.append(doc)
    return emp
# update employee salary based on the given id
# delete employee
@app.delete("/deleteEmployee")
async def delete_Student(id:int):
    '''this method is used to delete Employee base don the  given id'''
    if collection.find_one({"empid":id}) is None:
        return {"error":"id not found"}
    collection.delete_one({"empid":id})
    return {"message":"sucesfully deleted"}