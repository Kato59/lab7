def remove_element(array, item):
    try:
        array.remove(item)
    except ValueError:
        pass  # Если элемент не найден, ничего не делаем


# Пример использования:
array = [1, 2, 3, 4, 5, 6, 7]
remove_element(array, 5)
print(array)  # Результат: [1, 2, 3, 4, 6, 7]

array = ["Kiev", "Beijing", "Lima", "Saratov"]
remove_element(array, "Lima")
remove_element(array, "Berlin")  # Ничего не делает
print(array)  # Результат: ['Kiev', 'Beijing', 'Saratov']
