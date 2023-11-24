def sort_list_imperative(numbers):
    # Устанавливаем flag в True, чтобы цикл запустился хотя бы один раз
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                # Меняем элементы
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                # Устанавливаем flag в True для следующей итерации
                flag = True

    return numbers

# numbers = [10, 2, 7, -2, 6, 15, 4, 78, 0, -5]

print(sort_list_imperative([10, 2, 7, -2, 6, 15, 4, 78, 0, -5]))
