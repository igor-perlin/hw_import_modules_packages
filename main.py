from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date

employees = ['Перлин Игорь', 'Чуднова Наташа']

if __name__ == '__main__':
    print(f'Данные по сотрудникам и зарплатам на {datetime.today().date()}')
    print('-' * 50)
    print('Сотрудники:')
    get_employees(employees)
    print('-' * 50)
    print('Зарплаты:')
    calculate_salary(employees[0], 1850, 24)
    calculate_salary(employees[1], 2540, 24)
