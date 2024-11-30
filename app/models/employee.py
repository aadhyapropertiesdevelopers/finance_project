class Employee:
    def __init__(self, emp_id, name, phone_number, branch, address, role):
        self.id = emp_id
        self.name = name
        self.phone_number = phone_number
        self.branch = branch
        self.address = address
        self.role = role

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "branch": self.branch,
            "address": self.address,
            "role": self.role
        }
