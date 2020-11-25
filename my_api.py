from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from html_responds import return_employee_html
from es import add_employee_es, get_employee_es, update_employee_es, delete_employee_es, get_all_employees_es
from constants import *

app = FastAPI()

# GET methods - get record
@app.get('/')
def home():
    return {"message": "Hello World"}


@app.get('/employees')
def return_employees():
    """
    :return: list of dict with employees details
    """
    return get_all_employees_es()


@app.get('/employees/{employee_id}')
def return_employee(employee_id: int):
    """Display details about Employee from DB. Once return html or HTTPException(html for learning purposes - I am aware that should return json in boths situations)"""
    employee_dict = get_employee_es(employee_id)
    if employee_dict is None:
        raise HTTPException(status_code=404, detail=f'Employee with id {employee_id} do not exists')
    return return_employee_html(employee_dict)


# Post methods - New record

class Employee(BaseModel):
    id: int
    name: str
    surname: str
    position: str
    salary: int = 0

    def to_json(self):
        return self.__dict__


@app.post('/employees/')
def add_employee(employee: Employee):
    result = add_employee_es(employee.id, employee.to_json())
    if result:
        return 'Success'
    else:
        return 'Failure'



# Put methods - update record


@app.put('/employees/')
def update_employee(employee: Employee):
    pass



# Delete methods

@app.delete('/employees/{employee_id}')
def delete_employees(employee_id: int):
    pass








