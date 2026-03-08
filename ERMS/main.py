from ERMS.reportingSystem import total_employees, highest_paid_employee, dept_wise_salary_expense, active_projects, \
    monthly_payroll_summary
from employee import Employee
from user import User
from department import Department
from payroll import Payroll
from projectAssignment import Project
import reportingSystem

class WrongChoice(Exception):
    pass

currentUser = None
emp_list = []
dept_list = []
project_list = []
def login():
    global currentUser
    try:

        while True:
            choice = int(input(f'What would you like to do? \n 1. Login \n 2. Change Password \n3. Exit\n Please enter choice'))
            if choice == 1:
                username = input("Please enter username: ").strip()
                password = input("Please enter password: ").strip()
                role = input("Please enter role").strip()
                user1 = User(username, password, role)
                if user1.login():
                    currentUser = user1
                    print("Login Successful....")
                    break
            elif choice == 2:
                username = input("Please enter username: ").strip()
                password = input("Please enter password: ").strip()
                role = input("Please enter role").strip()
                newPassword = input("Please enter new password").strip()
                user1 = User(username, password, role)
                changed = user1.change_password(newPassword)
                if changed:
                    print("Password Changed")
            elif choice == 3:
                break
            else:
                raise WrongChoice("Error: Please input valid entry")


    except ValueError:
        print("Error: Please enter valid entry")
    except WrongChoice:
        print("Error: Please pick from the choices given")

def employee_management():
    try:
        while True:
            choice = int(input(f'What would you like to do?\n1. Create new employee \n 2. Update Salary \n 3. Calculate Annual Salary \n4. Display Your Details \n5. Exit \n Please enter choice'))
            if choice == 1:
                if currentUser.role == 'Admin':
                    employee_id = int(input("Please enter employee Id: ").strip())
                    name = input("Please enter Name:").strip()
                    dept = input("Please enter Department:").strip()
                    salary = int(input("Please enter Salary:").strip())
                    joining_date = input("Please joining date in format yyyy-mm-dd").strip()
                    leave_days = int(input("Please enter no of leave days").strip())
                    emp1 = Employee(employee_id, name, dept, salary,joining_date,leave_days)

                    if emp1 not in emp_list:
                        emp_list.append(emp1)
                        print("Employee added")

                else:
                    print("Access denied: only admin can access this")
            elif choice == 2:
                if currentUser.role == 'Admin':
                    emp_id = int(input("Please enter employee id that you would like to update salary:").strip())
                    newSalary = int(input("Please enter new salary").strip())
                    for emp in emp_list:
                        if emp.employee_id == emp_id:
                            done = emp.update_salary(newSalary)
                            if done:
                                print("Salary updated")
                else:
                    print("you don't have access to this tab")

            elif choice == 3:
                for emp in emp_list:
                    print(f' Salary of {emp.employee_id} is {emp.calculate_annual_salary()}')
            elif choice == 4:
                for emp in emp_list:
                    emp.display_details()
            elif choice == 5:
                break
            else:
                raise WrongChoice

    except ValueError:
        print("Error: Please enter valid entry")
    except WrongChoice:
        print("Error: Please pick from the choices given")

def department_management():
    try:
        while True:
            choice = int(input(f'What would you like to do?\n1. Create Department\n 2. Add employee \n 3. Remove Employee \n4. Total Department Expense\n 5. Exit \n Please enter choice'))
            if choice ==1:
                if currentUser.role == 'Admin':
                    dept_id = int(input("Please enter dept id:").strip())
                    dept_name = input("Please enter dept name:").strip()
                    dept1 = Department(dept_id, dept_name)


                    if dept1 not in dept_list:
                        dept_list.append(dept1)

                else:
                    print("You don't have access to this tab")
            elif choice == 2:
                if currentUser.role == 'Admin' and len(dept_list) != 0:
                    id = int(input("Please enter dept id:").strip())
                    emp_id = int(input("Please enter employee id that you would like to add to this department:").strip())
                    for dept in dept_list:
                        if dept.dept_id == id:
                            for emp in emp_list:
                                if emp.employee_id == emp_id:
                                    done = dept.add_employee(emp)
                                    if done:
                                        print("Employee added to department")
                                    else:
                                        print("Error adding given employee")
                        else:
                            print("Department with entered department id doesn't exists")

                else:
                    print("You don't have access to this tab")

            elif choice == 3:
                if currentUser.role == 'Admin' and len(dept_list) != 0:
                    id = int(input("Please enter dept id:").strip())
                    emp_id = int(input("Please enter employee id that you would like to add to this department:").strip())
                    for dept in dept_list:
                        if dept.dept_id == id:
                            for emp in emp_list:
                                if emp.employee_id == emp_id:
                                    done = dept.remove_employee(emp)
                                    if done:
                                        print("Employee added to department")
                                    else:
                                        print("Error adding given employee")
                        else:
                            print("Department with entered department id doesn't exists")

                else:
                    print("You don't have access to this tab")


            elif choice == 4:
                dept_id = int(input("Enter department id: ").strip())

                for dept in dept_list:
                    if dept.dept_id == dept_id:
                        dept.total_department_expense()

            elif choice == 5:
                break

            else:
                raise WrongChoice

    except ValueError:
        print("Error: Please enter valid entry")

    except WrongChoice:
        print("Error: Please pick from the choices given")


def project_assignment():
    try:

        global project_list
        while True:
            choice = int(input(f'What would you like to do?\n1. Create Project\n 2. Add employee \n 3. Remove Employee \n4. List Members\n 5. Exit \n Please enter choice'))

            if choice == 1:
                if currentUser.role == 'Manager' or currentUser.role == 'Admin':
                    project_id = int(input("Please enter Project id:").strip())
                    project_name = input("Please enter Project name:").strip()
                    project1 = Project(project_id, project_name)

                    if project1 not in project_list:
                        project_list.append(project1)
                else:
                    print("You don't have access to this tab")
            elif choice == 2:
                if currentUser.role == 'Admin' or currentUser.role == 'Manager':
                    project_id = int(input("Please enter Project id that you want to work on:").strip())

                    emp_id = int(input("Please enter employee id that you would like to add to this project:").strip())
                    for project in project_list:
                        if project.project_id == project_id:
                            for emp in emp_list:
                                if emp.employee_id == emp_id:
                                    done = project.assign_employee(emp)
                                    if done:
                                        print("Employee added...")
                                    else:
                                        print("Error adding employee...")
                        else:
                            print("No project with this project id exists...")
                else:
                    print("You don't have access to this tab")

            elif choice == 3:
                if currentUser.role == 'Admin' or currentUser.role == 'Manager':
                    project_id = int(input("Please enter Project id that you want to work on:").strip())

                    emp_id = int(input("Please enter employee id that you would like to add to this project:").strip())
                    for project in project_list:
                        if project.project_id == project_id:
                            for emp in emp_list:
                                if emp.employee_id == emp_id:
                                    done = project.remove_employee(emp)
                                    if done:
                                        print("Employee removed...")
                                    else:
                                        print("Error removing employee...")

                        else:
                            print("No project with this project id exists...")
                else:
                    print("You don't have access to this tab")


            elif choice == 4:
                project_id = int(input("Please enter Project id that you want to work on:").strip())


                for project in project_list:
                    if project.project_id == project_id:
                        project.list_project_members()
                    else:
                        print("No project with this project id exists...")

            elif choice == 5:
                break


            else:
                raise WrongChoice

    except ValueError:
        print("Error: Please enter valid entry")

    except WrongChoice:
        print("Error: Please pick from the choices given")


def payroll_processing():
    try:
        p1 = None
        while True:
            choice = int(input(f'What would you like to do?\n1. Create Payroll \n 2. Calculate Tax \n3. Generate PaySlip \n4. Deduct leave\n5. Exit \n Please enter choice'))

            if choice == 1:
                emp_id = int(input("Please Enter Employee ID: ").strip())

                emp_found = None
                for emp in emp_list:
                    if emp.employee_id == emp_id:
                        emp_found = emp

                if emp_found:
                    p1 = Payroll(emp_found)
                    print("Payroll created successfully")
                else:
                    print("Error: Employee not found")

            elif choice in range(2,6):
                if p1 is None:
                    print("Please create payroll first")
                    continue
                if choice == 2:
                    print(f"Calculated Tax: {p1.calculate_tax()}")
                elif choice == 3:
                    print(f'Your Salary Slip is: {p1.generate_salary_slip()}')

                elif choice == 4:
                    if currentUser.role == 'Admin':
                        print(f'Leave deduction for current employee is: {p1.deduct_leave()}')
                    else:
                        print("You don't have access to this tab")
                elif choice == 5:
                    break

            else:
                raise WrongChoice

    except ValueError:
        print("Error: Please enter valid entry")

    except WrongChoice:
        print("Error: Please pick from the choices given")

def generate_reports():
    try:
        while True:
            choice = int(input(f'Which Report you want to generate Bro?\n1. Total employees \n2. Highest paid employee \n3. Department-wise salary expense\n4. Active projects\n5. Monthly payroll summary\n 6. Exit\n Please enter choice'))


            if choice == 1:
                if currentUser.role == 'Admin' or currentUser.role == 'Manager':
                    print(f'Total Employees in company: {total_employees()}')

                else:
                        print("You don't have access to this tab")
            elif choice == 2:
                print(f'Highest paid employee: {highest_paid_employee()}')


            elif choice == 3:
                if currentUser.role == 'Admin' or currentUser.role == 'Manager':
                    dept_wise_salary_expense(dept_list)

                else:
                    print("You don't have access to this tab")
            elif choice == 4:
                if currentUser.role == 'Admin' or currentUser.role == 'Manager':
                    active_projects(project_list)

                else:
                    print("You don't have access to this tab")
            elif choice == 5:
                if currentUser.role == 'Admin' or currentUser.role == 'Manager':
                    monthly_payroll_summary(emp_list)

                else:
                    print("You don't have access to this tab")
            elif choice == 6:
                break

            else:
                raise WrongChoice

    except ValueError:
        print("Error: Please enter valid entry")

    except WrongChoice:
        print("Error: Please pick from the choices given")




def menu():
    try:
        while True:
            choice = int(input("Menu: \n 1. Login \n 2. Employee Management \n 3. Department Management \n 4. Project Assignment \n 5. Payroll Processing \n 6. Generate Reports \n 7. Exit\n Please enter choice "))
            if choice == 1:
                login()

            elif choice == 2:
                if currentUser is None:
                    print("Please enter 1 for Login again")
                else:
                    employee_management()
            elif choice == 3:
                if currentUser is None:
                    print("Please enter 1 for Login again")
                else:
                    department_management()

            elif choice == 4:
                if currentUser is None:
                    print("Please enter 1 for Login again")
                else:
                    project_assignment()

            elif choice == 5:
                if currentUser is None:
                    print("Please enter 1 for Login again")
                else:
                    payroll_processing()
            elif choice == 6:
                if currentUser is None:
                    print("Please enter 1 for Login again")
                else:
                    generate_reports()

            elif choice == 7:
                break


    except ValueError:
        print("Error: Please enter valid entry")
    except WrongChoice:
        print("Error: Please pick from the choices given")



menu()

