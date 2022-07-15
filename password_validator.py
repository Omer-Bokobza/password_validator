import re
import sys
from colorama import Fore


def is_valid(password):
    if len(password) < 10:
        print(Fore.RED + "password length below 10")
        return False

    if not re.search('[0-9]', password):
        print(Fore.RED + "password missing numbers")
        return False

    if not re.search('[a-z]', password):
        print(Fore.RED + "password missing Lower case")
        return False

    if not re.search('[A-Z]', password):
        print(Fore.RED + "password missing Upper case")
        return False

    return True


if __name__ == "_main_":

    if is_valid(sys.argv[1]):
        print(Fore.GREEN + "password is valid")
        exit(0)
    else:
        exit(1)