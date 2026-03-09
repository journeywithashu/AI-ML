import json

json_str = '{"name": "ashu", "isTeacher": true}'

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)