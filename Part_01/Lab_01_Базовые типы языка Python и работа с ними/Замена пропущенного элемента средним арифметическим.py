numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
len_list = len(numbers)
new_numbers = numbers[:]
left_sum = 0
right_sum = 0

for i in range(len_list):
    if new_numbers[i] is None:
        left_sum = sum(new_numbers[:i])
        right_sum = sum(new_numbers[i + 1:len_list])
        new_numbers[i] = (left_sum + right_sum) / (len_list)

print("Измененный список:", new_numbers)