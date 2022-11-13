import random

def get_unique_list_numbers(size = 15, start = -10, stop = 10) -> list[int]:
    list_ = []

    while len(list_) < size:
        random_number = random.randint(start, stop)
        if random_number not in list_:
            list_.append(random_number)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
