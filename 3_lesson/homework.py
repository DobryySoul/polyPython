import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series

# - списки Python или массивы NumPy

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series(np.array([1, 2, 3, 4, 5]))
print(series1)
print(series2)

# - скалярные значение

series3 = pd.Series(5, index=[0, 1, 2, 3, 4])
print(series3)

# - словари

series4 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(series4)

# 2. Привести различные способы создания объектов типа DataFrame

# - через объекты Series

df1 = pd.DataFrame({
    'a': pd.Series([1, 2, 3, 4, 5]),
    'b': pd.Series([5, 4, 3, 2, 1]),
    'c': pd.Series([1, 2, 3, 4, 5]),
    'd': pd.Series([5, 4, 3, 2, 1]),
    'e': pd.Series([1, 2, 3, 4, 5])
})

print(df1)

# - списки словарей

df2 = pd.DataFrame([
    {'a': 1, 'b': 5, 'c': 1},
    {'a': 2, 'b': 4, 'c': 2},
    {'a': 3, 'b': 3, 'c': 3},
    {'a': 4, 'b': 2, 'c': 4},
    {'a': 5, 'b': 1, 'c': 5},
])

print(df2)

# - словари объектов Series

df3 = pd.DataFrame({
    'a': pd.Series([1, 2, 3, 4, 5]),
    'b': pd.Series([5, 4, 3, 2, 1]),
    'c': pd.Series([1, 2, 3, 4, 5]),
    'd': pd.Series([5, 4, 3, 2, 1]),
    'e': pd.Series([1, 2, 3, 4, 5])
})

print(df3)

# - двумерный массив NumPy

df4 = pd.DataFrame(np.array([[1, 5, 1], [2, 4, 2], [3, 3, 3], [4, 2, 4], [5, 1, 5]]))

print(df4)

# - структурированный массив Numpy

df5 = pd.DataFrame(np.array(
    [(1, 5, 1), (2, 4, 2), (3, 3, 3), (4, 2, 4), (5, 1, 5)], 
    dtype=[('a', int), ('b', int), ('c', int)]
))

print(df5)

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1

pop = pd.Series({
    "city_1": 1001,
    "city_2": 1002,
    "city_3": 1003,
    "city_41": 1004,
    "city_51": 1005,
})

area = pd.Series({
    "city_1": 9991,
    "city_2": 9992,
    "city_3": 9993,
    "city_42": 9994,
    "city_52": 9995,
})

combined = pop.add(area)
combined = combined.fillna(1)
print(combined)

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

rng = np.random.default_rng()

A = rng.integers(0, 10, (3, 4))
df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])

print(df)
print(df.subtract(df['a'], axis=0))

# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

rng = np.random.default_rng()

A = rng.integers(0, 10, (3, 4))
data_frame = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])

print(data_frame)

data_frame.iloc[1, 1] = np.nan
data_frame.iloc[2, 2] = np.nan

print(data_frame)

ffill_df = data_frame.ffill()
print(ffill_df)

bfill_df = data_frame.bfill()
print(bfill_df)
