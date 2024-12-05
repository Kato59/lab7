def unique(array):
    return list(dict.fromkeys(array))  # Используем dict для сохранения порядка


# Пример использования:
result = unique([2, 1, 1, 3, 2])
print(result)  # Результат: [2, 1, 3]

result = unique(["top", "bottom", "top", "left"])
print(result)  # Результат: ['top', 'bottom', 'left']
