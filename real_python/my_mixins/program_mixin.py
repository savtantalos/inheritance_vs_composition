import json
from real_python.employees import EmployeeDatabase


def print_dict(d):
    print(json.dumps(d, indent=2))


for employee in EmployeeDatabase().employees:
    print_dict(employee.to_dict())
