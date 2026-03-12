#question 1
import pandas as pd
from sqlalchemy import create_engine
import csv

#creating bridge between user and server
engine = create_engine('mysql+pymysql://root:SUMEETgur10@localhost:3306/company_db')

#query to read from database to verify all tables in database
query = "SHOW TABLES"
#reading tables from database
with engine.connect() as conn:
    table_names_df = pd.read_sql(
        sql = query,
        con = conn.connection
    )

print(f'Printing all tables in Company data: \n {table_names_df}')
print(f'\n............................\n')

#question2
#reading all data from employees
query2 = "SELECT * FROM employees"
with engine.connect() as conn:
    company_df = pd.read_sql(
        sql = query2,
        con = conn.connection
    )

print(f'Printing first 5 rows: \n {company_df.head(5)}')
print(f'Printing dataframe info: \n {company_df.info()}')
print(f'Describing database: \n {company_df.describe()}')
print(f'\n............................\n')

#question 3
#display emp with exp > 5yrs and salary > 60000
filtered_df = company_df[(company_df['experience'] > 5) & (company_df['salary'] > 60000)]
print(f'Data of Employees with experience > 5 years and salary > 60000: \n {filtered_df[['name', 'department', 'salary']]}')
print(f'\n............................\n')

#question 4
avg_salary_by_dept = company_df.groupby('department')['salary'].mean()
print(f'Average salary by department: \n {avg_salary_by_dept}')
print(f'\n............................\n')

max_exp_per_location = company_df.groupby('location')['experience'].max()
print(f'Maximum experience by location: \n {max_exp_per_location}')
print(f'\n............................\n')

total_salary_exp_dept = company_df.groupby('department')['salary'].sum()
print(f'Total salary expenditure by department: \n {total_salary_exp_dept}')
print(f'\n............................\n')

#question 5
def salary_wise_label(salary):
    if salary > 80000:
        return "High"
    elif (salary > 50000) and (salary <= 80000):
        return "Medium"
    elif (salary >= 0) and (salary <= 50000):
        return "Low"
    else:
        return None

new_column_data = company_df['salary'].apply(salary_wise_label)

company_df["performance_level"] = new_column_data
filtererd_display = company_df[['name','department', 'salary', 'performance_level']]
print(f'Company data with new column added: \n {filtererd_display}')
print(f'\n............................\n')

#question 6
#adding tabel to database
print(f'Adding new table to Company database.....\n')
tabel_name = 'employee_summary'
company_df.to_sql(
    name = tabel_name,
    con = engine,
    if_exists= 'replace',
    index = False
)
print(f'New table added to database.....\n')

#writing to csv file
print(f'Writing to csv.....\n')
company_df.to_csv('/Users/harsimransidhu/PycharmProjects/PragraLearning/employee_summary.csv',
                  index = False)
print(f'Writing done.....\n')


