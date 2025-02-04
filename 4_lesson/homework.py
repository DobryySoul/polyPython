import pandas as pd
import numpy as np

# 1. Разобраться как использовать мультииндексные ключи в данном примере
index1 = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

# Для реализации мультииндексовых ключей
index_multi = pd.MultiIndex.from_tuples(index1)

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]
pop = pd.Series(population, index=index_multi)
pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)


pop_df_1 = pop_df.loc['city_1', 'something']
print(pop_df_1)
pop_df_1 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
print(pop_df_1)
pop_df_1 = pop_df.loc[['city_1', 'city_3'], 'something']
print(pop_df_1)

# 2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2 

data_dic = {
    ('city_1', 2010): 100,
    ('city_1', 2020): 200,
    ('city_2', 2010): 1001,
    ('city_2', 2020): 2001,
}

s = pd.Series(data_dic)
print(s)

s.index.names = ['city', 'year']
print(s)

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020],
    ],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2'],
    ],
    names=['worker', 'job']
)
rng = np.random.default_rng(1)

data = rng.random((4, 6))

data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)

# - 2020 году (для всех столбцов)
print(data_df.loc[:, 2020, :])

# - job_1 (для всех строк)
print(data_df.loc[:, (['person_1', 'person_2', 'person_3'], 'job_1')])

# - для city_1 и job_2
print(data_df.loc[('city_1', [2010, 2020]), (['person_1', 'person_2', 'person_3'], 'job_2')])


# 3. Взять за основу DataFrame со следующей структурой
index3 = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns3 = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)
#
# Приведите пример (самостоятельно) с использованием pd.IndexSlice

rng3 = np.random.default_rng(1)

data_frame = pd.DataFrame(rng3.random((4, 6)), index=index3, columns=columns3)
print(data_frame)

# - все данные по person_1 и person_3
print(data_frame.loc[:, (['person_1', 'person_3'])])

# - все данные по первому городу и первым двум person-ам (с использование срезов)
print(data_frame.loc['city_1', (['person_1', 'person_2'])])

# Приведите пример (самостоятельно) с использованием pd.IndexSlice
i = pd.IndexSlice
# - все данные по person_1 и person_3
print(data_frame.loc[i[:], i[['person_1', 'person_3']]])

# - все данные по первому городу и первым двум person-ам (с использование срезов)
print(data_frame.loc['city_1', i[:'person_2', :]])


#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['b', 'c', 'd'], index=[2, 3, 4])

print(pd.concat([ser1, ser2], axis=1, join='outer'))

print(pd.concat([ser1, ser2], axis=1, join='inner'))