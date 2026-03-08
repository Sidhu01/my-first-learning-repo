from employee import Employee

class InvalidEntry(Exception):
    pass

class DuplicateEntry(Exception):
    pass

class Department:
    def __init__(self, dept_id, dept_name, employee_list=None):
        self.dept_id = dept_id
        self.dept_name = dept_name
        if employee_list is None:
            self.employee_list = []
        else:
            self.employee_list = employee_list


    def add_employee(self, employee):
        try:
            if not isinstance(employee, Employee):
                raise InvalidEntry("Error: Please check employee")

            #check duplicate employee entry
            for i in self.employee_list:
                if i.employee_id == employee.employee_id:
                    raise DuplicateEntry("Error: employee already in Department")
            self.employee_list.append(employee)
            return True

        except InvalidEntry:
            print("Error: Please check employee")
            return False
        except DuplicateEntry:
            print("Error: employee already in Department")
            return False

    def remove_employee(self, employee):
        try:
            if not isinstance(employee, Employee):
                raise InvalidEntry("Error: check employee attribute")
            if employee not in self.employee_list:
                raise InvalidEntry("Error: Given Employee Id doesn't exist in this department")
            self.employee_list = [ i for i in self.employee_list if i.employee_id != employee.employee_id]
            return True

        except InvalidEntry:
            print("Error: Given Employee Id doesn't exist in this department")
            return False
        except ValueError:
            print("Error: Value mismatch")
            return False

    def total_salary_expense(self):
        expense = 0
        for i in self.employee_list:
            expense = expense + i.calculate_annual_salary()

        return expense

