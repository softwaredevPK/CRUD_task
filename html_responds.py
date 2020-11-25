"""
Module with functions which returns html code
"""

from fastapi.responses import HTMLResponse


def return_employee_html(id_, name, surname):
    html_content = f"""
    <html>
        <head>
            <title>employee_id:{id_}</title>
        </head>
        <body>
            <h1>Details about employee: {id_}</h1>
            <p>Name: {name} <br/> Surname: {surname}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)








