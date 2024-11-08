numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_lost_el = 4
numbers[index_lost_el] = 0
average = sum(numbers)/len(numbers)
numbers[index_lost_el] = average
print("Измененный список:", numbers)
