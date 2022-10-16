list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_numbers = list_numbers[0]
for i in list_numbers:
    if i > max_numbers:
        max_numbers = i
index = list_numbers.index(max_numbers)
list_numbers[index], list_numbers[-1] = list_numbers[-1], list_numbers[index]

print(list_numbers)
