
import json
salaryObject={
    "name": "Hafizue Rahman",
    "Designation" : "Sr.Developer",
    "Section":"Fullstack Developer ",
    "Salary":"80000 BDT"
}
# Python object convert to Json Object
print("Python object convert to Json")
salaryJason = json.dumps(salaryObject,indent=4)
print(salaryJason)

# Json String/Object convert to python object
print("Json String convert to python object")
jasonObj = '{"name": "Hafizue Rahman", "Designation": "Sr.Developer", "Section": "Fullstack Developer ", "Salary": "80000 BDT"}'
pythonObj = json.loads(jasonObj)
print(pythonObj)

pyList=[
    {"name": "a","Slary":"45000"},
    {"name": "b","Slary":"55000"},
    {"name": "c","Slary":"35000"},
    {"name": "d","Slary":"44000"},
]

# python list convert to Jason Array
print("python list convert to Jason Array")

jasonArray = json.dumps(pyList,indent=4)
print(jasonArray)