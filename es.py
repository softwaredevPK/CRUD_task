from elasticsearch import Elasticsearch

es = Elasticsearch(HOST="http://localhost", PORT=9200)


def add_employee_es(id, employee_json):
    es.index(index='megacorp', doc_type='employee', id=id, body=employee_json)


def get_employee_es(id):
    result = es.get(index='megacorp', doc_type='employee', id=id)
    return result['_source']


def delete_employee_es(id):
    es.delete(index='megacorp', doc_type='employee', id=id)


def update_employee_es(id, employee_json):
    if employee_json.get['doc'] is None:
        employee_json = {"doc": employee_json}
    es.update(index='megacorp', doc_type='employee', id=id, body=employee_json)

