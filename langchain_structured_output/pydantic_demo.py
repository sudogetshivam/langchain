from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'shivam'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float =  Field(gt=0,lt=10,description='A decimal value representing the cgpa of thw student')

new_student = {'age':'32','email':'xyz@gmail.com','cgpa':'8.59'}
student = Student(**new_student)

print(student)
print(type(student)) #pydantic object

student_json = student.model_dump_json()
print(student_json)