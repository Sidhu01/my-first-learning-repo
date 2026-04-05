import csv

class InvalidSalary(Exception):
    pass

class Employee:
    def __init__(self, employee_id, name, department, salary, joining_date, leave_days):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.joining_date = joining_date
        self.leave_days = leave_days

        self.add_employee() #adds employees to csv if not already there

    def add_employee(self):
        try:
            with open('/data/employee_records.csv',
                      mode='r') as file:
                reader = csv.reader(file)
                found = False
                next(reader,None)
                for data in reader:
                    if int(data[0]) == self.employee_id:
                        found = True
                        return False
            if not found:
                with open('/data/employee_records.csv', mode='a', newline='') as dataFile:
                    writer = csv.writer(dataFile)
                    data = [self.employee_id, self.name, self.department, self.salary, self.joining_date, self.leave_days]
                    writer.writerow(data)
                    return True
            return False


        except FileNotFoundError:
            print("Error: file not found")
            return False
        except ValueError:
            print("Error: Missing Value")



    def update_salary(self,salary):
        try:

             if not isinstance(salary, (int, float)) or salary < 0:
                raise InvalidSalary("Error: Please check salary amount should....")

             with open('/data/employee_records.csv', mode ='r') as file:
                 reader = csv.reader(file)
                 new_list = [['employee_id','name','department','salary','joining_date','leave_days']]
                 next(reader,None)
                 for data in reader:
                     if int(data[0]) == self.employee_id:
                        data[3] = str(salary)
                        self.salary = salary

                     new_list.append(data)

             with open('/data/employee_records.csv', mode='w', newline='') as dataFile:
                writer = csv.writer(dataFile)
                writer.writerows(new_list)
                return True

        except InvalidSalary:
            print("Error: Please check salary amount should....")
            return False
        except FileNotFoundError:
            print("Error: file not found")
            return False
        except IndexError:
            print("Error: Missing Values")
            return False
        except ValueError:
            print("Error: Value Mismatch")
            return False
        except TypeError:
            print("Error: Empty file")







    def calculate_annual_salary(self):
        return self.salary * 12

    def display_details(self):
        print( f'Employee Id : {self.employee_id} \n Employee Name: {self.name} \n Department: {self.department} \n Salary: {self.salary} \n Joining date: {self.joining_date}')

