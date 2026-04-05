from employee import Employee
from user import User
from department import Department
from payroll import Payroll
from projectAssignment import Project
import csv



def total_employees():
    try:
        with open('/data/employee_records.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)
            count = 0

            for data in reader:
                count +=1
            return count

    except FileNotFoundError:
        print("Error: File not found")
        return 0

def highest_paid_employee():
    try:
        with open('/data/employee_records.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader,None)
            data = list(reader)
            max_salary = 0
            emp_max = []

            for line in data:
                if int(line[3]) >= max_salary:
                    max_salary = int(line[3])
            max_salary_list = [line[:4] for line in data if int(line[3]) == max_salary]
            return max_salary_list

    except FileNotFoundError:
        print("Error: File not found")
        return None
    except IndexError:
        print("Error: Missing Value")
        return None
    except ValueError:
        print("Error: Value Mismatch")
        return None
    except TypeError:
        print("Error: Wrong type")
        return None


def dept_wise_salary_expense(list_of_departments):
    output= []
    for  department in list_of_departments:
        output.append({'Department Id' : department.dept_id ,
                  'Department Name' : department.dept_name,
                  'Total Expense' : department.total_salary_expense()
                  })

    for i in output:
        print(f'{i}\n')

def active_projects(list_of_projects):
    output = []
    for project in list_of_projects:
        output.append({'Project Id': project.project_id,
                       'Project Name': project.project_name,
                       'List of Employees': project.list_project_members()
                       })

    for i in output:
        print(f'{i}\n')

def monthly_payroll_summary(list_of_employees):
    print("Monthly Payroll Summary")
    for emp in list_of_employees:
        payroll = Payroll(emp)
        payroll.generate_salary_slip()









