def remove_elements(array, *items):
    for item in items:
        try:
            array.remove(item)
        except ValueError:
            pass  # Игнорируем отсутствующие элементы


# Пример использования:
array = [1, 2, 3, 4, 5, 6, 7]
remove_elements(array, 5, 1, 6)
print(array)  # Результат: [2, 3, 4, 7]

array = ["Kiev", "Beijing", "Lima", "Saratov"]
remove_elements(array, "Lima", "Berlin", "Kiev")
print(array)  # Результат: ['Beijing', 'Saratov']
