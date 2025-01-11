import numpy as np
import array

## Задача 1

'''
'b' целое число со знаком, 1 байт
'B' целое число без знака, 1 байт
'h' целое число со знаком, 2 байта
'H' целое число без знака, 2 байта
'i' целое число со знаком, 4 байта
'I' целое число без знака, 4 байта
'q' целое число со знаком, 8 байта
'Q' целое число без знака, 8 байта
'f' вещественное число, 4 байта
'd' вещественное число, 8 байт
и т.д.
'''

## Задача 2

arr_b = array.array('b', [1, -2, 3, -4, 5])
arr_i = array.array('i', [1, -2, 3, -4, 5])
arr_I = array.array('I', [1, 2, 3, 4, 5])
arr_f = array.array('f', [1.0, 2.0, 3.0, 4.0, 5.0])
print(arr_b)
print(arr_i)
print(arr_I)
print(arr_f)

## Задача3

arr = np.linspace(0, 1, 5)
print(arr)

## Задача 4

arr = np.random.rand(5)
print(arr)

## Задача 5

arr = np.random.normal(0, 1, 5)
print(arr)

## Задача 6

arr = np.random.randint(0, 10, 5)
print(arr)

## Задача 7

arr = np.array([i for i in range(12)]).reshape(3,4)
print("Оригинальный массив:", arr)
print("первые две строки и три столбца:", arr[:2, :3])
print("первые три строки и второй столбец:", arr[:3, 1:2])
print("все строки и столбцы в обратном порядке:", arr[::-1, ::-1])
print("второй столбец:", arr[:, 1:2])
print("третья строка:", arr[2:3, :])

## Задача 8

arr = np.array([1, 2, 3, 4, 5])
b = arr.copy()[1:4]
print("Original array:", arr)
print("Slice-duplicate:", b)
b[2] = 52
print("Original slice after the changing to a slice-duplicate:", arr)
print("Slice-duplicate after the change:", b)

## Задача 9

a = np.array([1, 2, 3])
b = a[:, np.newaxis]
c = a[np.newaxis, :]
print("Vector-column:", b)
print("Vector-row:", c)

## Задача 10

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Переставляет один массив за другой, условно делая первый невидимым, 
# если смотреть спереди, но видимым сверху
r1 = np.dstack((x, y))
print("Method dstack:", r1)

## Задача 11

a = np.array([1, 2, 3, 4, 5, 6])
result1 = np.split(a, 3)  # Разделение на 3 части
print("Method split:", result1)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Разделение массива по вертикальной части на число indices
# необходимо, чтобы количество столбцов в массиве было кратно количеству частей
result2 = np.vsplit(b, 3)
print("Method vsplit:", result2)

c1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Разделение массива по горизонтальной части на число indices 
# Необходимо, чтобы количество столбцов в массиве было кратно количеству частей
result3 = np.hsplit(c1, 3)
result4 = np.hsplit(c2, 3)
print("Method hsplit:", result3)
print("Method hsplit:", result4)

d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Разделяет 3-х мерный массив вдоль 3 оси
# Требует, чтобы размерность по третьей оси была кратна количеству частей
result4 = np.dsplit(d, 2)
print("Method dsplit:", result4)

## Задача 12

arr1 = np.arange(3, 16, 3)
print("Add:",np.add(arr1, 3))
print("Subtract:", np.subtract(arr1, 3))
print("Negative:", np.negative(arr1))
print("Divide:", np.divide(arr1, 3))
print("Power:", np.power(arr1, 3))

arr2 = np.arange(1, 6)
print("Floor_divide:", np.floor_divide(arr2, 3))
print("Mod:", np.mod(arr2, 3))
