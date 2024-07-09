import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees


createBonusColumn(pd.DataFrame({
    'name': ['Piper', 'Grace'],
    'salary': [4548, 28150]
}))
