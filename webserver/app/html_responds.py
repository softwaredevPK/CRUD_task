"""
Module with functions which returns html code
"""

from fastapi.responses import HTMLResponse
from constants import *


def return_employee_html(employee_dict):
    html_content = f"""
    <html>
        <head>
            <title>employee_id:{employee_dict[ID]}</title>
        </head>
        <body>
            <h1>Details about employee: {employee_dict[ID]}</h1>
            <p>Name: {employee_dict[NAME]} <br/> 
               Surname: {employee_dict[SURNAME]} <br/> 
               Position: {employee_dict[POSITION]} <br/> 
               Salary" {employee_dict[SALARY]}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)








