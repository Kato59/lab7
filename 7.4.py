def difference(array1, array2):
    return [item for item in array1 if item not in array2]


# Пример использования:
array1 = [7, -2, 10, 5, 0]
array2 = [0, 10]
result = difference(array1, array2)
print(result)  # Результат: [7, -2, 5]

array1 = ["Beijing", "Kiev"]
array2 = ["Kiev", "London", "Baghdad"]
result = difference(array1, array2)
print(result)  # Результат: ['Beijing']
