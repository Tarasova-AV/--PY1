from pprint import pprint

def get_list_dict():
    list_dict = []
    for i in range(0, 16):
        dict_ = {i: b for i, b in [('bin', bin(i)), ('dec', i), ('oct', oct(i)), ('hex', hex(i))]}
        list_dict.append(dict_)
    return list_dict

pprint(get_list_dict())
