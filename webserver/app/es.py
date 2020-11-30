from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from constants import *

es = Elasticsearch(HOST="http://localhost", PORT=9200)


def add_employee_es(id, employee_json):
    # check if such employee exists
    if get_employee_es(id) is not None:
        return False
    # Add data
    try:
        es.index(index=MEGACORP, doc_type=EMPLOYEE, id=id, body=employee_json)
    except:
        return False
    else:
        return True


def get_employee_es(id):
    try:
        result = es.get(index=MEGACORP, doc_type=EMPLOYEE, id=id)
    except NotFoundError:
        return None
    else:
        return result[SOURCE]


def delete_employee_es(id):
    try:
        es.delete(index=MEGACORP, doc_type=EMPLOYEE, id=id)
    except NotFoundError:
        return False
    else:
        return True


def update_employee_es(id, employee_json):
    # check if json contains 'DOC'
    if employee_json.get(DOC) is None:
        employee_json = {DOC: employee_json}
    try:
        es.update(index=MEGACORP, doc_type=EMPLOYEE, id=id, body=employee_json)
    except NotFoundError:
        return False
    else:
        return True


def get_all_employees_es():
    result_list = []
    results = es.search(index=MEGACORP)[HITS][HITS]
    for index in range(len(results)):
        result_list.append(results[index][SOURCE])
    return result_list