import json

from hr_singleton import calculate_payroll
from productivity_singleton import track
from employees_singleton import employee_database, Employee

def print_dict(d):
    print(json.dumps(d, indent=2))

employees = employee_database.employees

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print('Temporary Secretary:')
print_dict(temp_secretary.to_dict())