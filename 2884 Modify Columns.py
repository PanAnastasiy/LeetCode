import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees


employees = pd.DataFrame({'name': ['John', 'Ann', 'Kale', 'Dion', 'Robert'], 'salary': [1, 2, 3, 4, 5]})
print(modifySalaryColumn(employees))