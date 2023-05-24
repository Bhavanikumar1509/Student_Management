"""
this is a student Management project using python FastAPI and mongodb


"""
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient('mongodb://172.17.0.2:27017/')
'''docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name> 
to find the  mongo db container ipaddress
'''
db = client['mydatabase']
collection = db['mycollection']

app = FastAPI()
class Student(BaseModel):
    '''this is student class with parameters id,name, age and marks'''
    id:int
    name:str
    age:int
    marks:int

    
@app.get("/students")
async def get_students():
    '''this method is used to get all the studdents using get API Call'''
    data = []
    for doc in collection.find():
        # convert the ObjectId to string
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return data


#create a student
@app.post("/createStudent")
async def create_new_student(student: Student):
    '''this method is use for creating a new student'''
    user_data = student.dict()
    result = collection.insert_one(user_data)
    return {'message': 'User added successfully', 'id': str(result.inserted_id)}

#update student by id
@app.patch("/UpdateStudents")
async def update_student(id:int, student:Student):
    '''this method is used to update student'''
    if collection.find_one({"id":id}) is None:
        return {"error":"id not found"}
    update_data=student.dict(exclude_unset=True)
    result = collection.update_one({"id": id}, {"$set": update_data})
    if result.modified_count == 1:
        return {"message": "Student updated successfully"}
    else:
        return {"error": "Failed to update student"}
@app.delete("/deleteStudents")
async def delete_Student(id:int):
    '''this method is used to delte student id based on the gicen id'''
    if collection.find_one({"id":id}) is None:
        return {"error":"id not found"}
    collection.delete_one({"id":id})
    return {"message":"sucesfully deleted"}


#get students based on their age
@app.get("/student/age")
async def student_by_age(age:int):
    stud=[]
    k=collection.find({"age":age})
    for doc in k:
        doc['_id'] = str(doc['_id'])
        stud.append(doc)
    return stud
         
#get students based on their marks
#get student by id


