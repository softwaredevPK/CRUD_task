from fastapi import FastAPI
from pydantic import BaseModel
from html_responds import return_employee_html


app = FastAPI()

# GET methods - get record
@app.get('/')
def home():
    return {"message": "Hello World"}


@app.get('/employees')
def return_employees():
    return


@app.get('/employees/')
def return_employee(employee_id: int = None, employee_name: str = None, employee_surname: str = None):
    """Display details about Employee from DB"""
    return return_employee_html(employee_id, employee_name, employee_surname)


# Post methods - New record

class Employee(BaseModel):
    id: int
    name: str
    surname: str


@app.post('/employees/')
def add_employee(employee: Employee):
    pass



# Put methods - update record


@app.put('/employees/')
def update_employee(employee: Employee):
    pass



# Delete methods

@app.delete('/employees/{employee_id}')
def delete_employees(employee_id: int):
    pass









