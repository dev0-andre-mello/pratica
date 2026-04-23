employee_name = input('employee name: ')
salary = float(input('employee salary: '))
total_sales = float(input('total sales: '))

total_salary = salary + (total_sales * 0.15)
print(f'TOTAL = R${total_salary:.2f}')

