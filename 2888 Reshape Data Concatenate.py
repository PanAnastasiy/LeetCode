import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])


df1 = pd.DataFrame({'student_id': [1, 2], 'name': ['Sofa', 'Jane'], 'age': [15, 66]})
df2 = pd.DataFrame({'student_id': [3, 4], 'name': ['Hole', 'Ann'], 'age': [25, 6]})
print(concatenateTables(df1, df2))
