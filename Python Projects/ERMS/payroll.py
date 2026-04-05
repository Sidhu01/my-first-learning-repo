from employee import Employee
from datetime import date, datetime

class Payroll:
    def __init__(self, employee):
        self.employee = employee

    def calculate_tax(self):
        try:
            salary = self.employee.calculate_annual_salary()
            tax = 0
            joining_date = datetime.strptime(self.employee.joining_date, "%Y-%m-%d").date()
            daysWorked = (date.today() - joining_date).days - self.employee.leave_days
            if daysWorked < 0:
                return 0
            till_date_salary = salary/365 * daysWorked

            if till_date_salary <= 53359:
                tax =  15
            elif till_date_salary <= 106717:
                tax =  20.5
            elif till_date_salary <= 165430:
                tax = 26
            elif till_date_salary <= 235675:
                tax =  29
            else:
                tax =  33

            tax_amount = till_date_salary * tax/100
            return tax_amount

        except ValueError:
            print("Error: Invalid Value")
            return None

    def deduct_leave(self):
        try:

            joining_date = datetime.strptime(self.employee.joining_date, "%Y-%m-%d").date()
            daysWorked = (date.today() - joining_date).days - self.employee.leave_days
            if daysWorked < 0:
                return 0

            daily_salary = self.employee.calculate_annual_salary()/365
            return daily_salary * self.employee.leave_days
        except ValueError:
            print("Error: Invalid Value")
            return None

    def generate_salary_slip(self):
        joining_date = datetime.strptime(self.employee.joining_date, "%Y-%m-%d").date()
        daysWorked = (date.today() - joining_date).days - self.employee.leave_days


        gross_income = self.employee.calculate_annual_salary()
        if daysWorked < 0:
            gross_income = 0 #if that is a future start date
        total_salary = gross_income - self.calculate_tax() - self.deduct_leave()
        print(f'Pay Slip of {self.employee.name} \n Employee Id: {self.employee.employee_id} \n Gross income: {gross_income} \n Net Income: {total_salary}')









