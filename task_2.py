# TODO посчитать количество каждой буквы в строке в аргументе str_
def get_count_char(str_):
    count_char = {}
    for char in str_.lower():
        if char.isalpha():
            if char in count_char:
                count_char[char] += 1
            else:
                count_char[char] = 1
    return count_char

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

dict_current = get_count_char(main_str)

def get_count_char_in_percent(dict_):
    for char in dict_:
        percent = 100
        dict_[char] = round(dict_[char] / sum(dict_.values()) * percent)
    return dict_
print(get_count_char_in_percent(dict_current))
