employee_name = str(input('Digite o seu nome: '))
employee_age = int(input('Digite a sua idade: '))
employee_salary = float(input('Digite o seu salário: '))
employee_zip_code = int(input('Digite o seu CEP: '))
employee_department = str(input('Digite seu departamento (Administrativo/Fábrica): '))

if len(employee_name) < 3:
    print('Nome menor que 3 caracteres!')

if employee_age < 0 or employee_age > 130:
    print('Idade inválida!')

if employee_salary < 0:
    print('Salário inválido!')

if employee_zip_code != 8:
    print('CEP inválido!')

if employee_department != 'Administrativo' or employee_department != 'Fábrica':
    print('Departamento inválido!')
