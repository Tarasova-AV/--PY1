import string
import random
def get_random_password(password_lenght = 8) -> str:
    possible_symbol_str = string.ascii_uppercase + string.ascii_lowercase + string.digits
    random_password_list = random.sample(possible_symbol_str, password_lenght)
    random_password_str = "".join([str(symbol) for symbol in random_password_list])
    return random_password_str

print(get_random_password())
