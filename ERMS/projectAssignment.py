from employee import Employee
class InvalidEntry(Exception):
    pass

class DuplicateEntry(Exception):
    pass

class Project:
    def __init__(self, project_id, project_name, assigned_employees=None):
        self.project_id = project_id
        self.project_name = project_name
        if assigned_employees is None:
            self.assigned_employees = []
        else:
            self.assigned_employees = assigned_employees

    def assign_employee(self, employee):
        try:
            if not isinstance(employee, Employee):
                raise InvalidEntry("Error: check employee attribute")
            for i in self.assigned_employees:
                if i.employee_id == employee.employee_id:
                    raise DuplicateEntry("Error: employee already in project")
            self.assigned_employees.append(employee)
            return True

        except InvalidEntry:
            print("Error: Please check employee")
            return False
        except DuplicateEntry:
            print("Error: employee already in project, duplicate entry")
            return False

    def remove_employee(self, employee):
        try:
            if not isinstance(employee, Employee):
                raise InvalidEntry("Error: check employee attribute")
            for data in self.assigned_employees:
                if data.employee_id == employee.employee_id:
                    new_list = [i for i in self.assigned_employees if i.employee_id != employee.employee_id]
                    self.assigned_employees = new_list
                    return True
            raise InvalidEntry("Error: Employee not found in project")

        except InvalidEntry:
            print("Error: Please check your entry")
            return False
        except ValueError:
            print("Error: Value mismatch")

    def list_project_members(self):
        output = []
        for emp in self.assigned_employees:
            output.append({"Employee Id": emp.employee_id,
            "Employee Name": emp.name,
            "Department": emp.department,
            "Salary": emp.salary,
            "Joining Date": emp.joining_date})

        return output

