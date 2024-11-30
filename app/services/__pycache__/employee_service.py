from models.employee import Employee

# Mock database
employees = []

def add_employee(employee_data):
    employee = Employee(**employee_data)
    employees.append(employee)
    return employee

def get_all_employees():
    return [employee.to_dict() for employee in employees]

def get_employee_by_id(emp_id):
    for employee in employees:
        if employee.id == emp_id:
            return employee.to_dict()
    return None

def update_employee(emp_id, updated_data):
    for employee in employees:
        if employee.id == emp_id:
            employee.name = updated_data.get("name", employee.name)
            employee.phone_number = updated_data.get("phone_number", employee.phone_number)
            employee.branch = updated_data.get("branch", employee.branch)
            employee.address = updated_data.get("address", employee.address)
            employee.role = updated_data.get("role", employee.role)
            return employee.to_dict()
    return None

def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if emp.id != emp_id]
    return True
