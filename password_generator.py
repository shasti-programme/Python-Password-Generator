import random
import string

all_strings = string.ascii_letters
all_integers = string.digits
special_chars = string.punctuation

i = 0
while i <= 3:
    random_strings = random.choice(all_strings)
    random_integers = random.choice(all_integers)
    random_special_chars = random.choice(special_chars)
    print(f"{random_strings.upper().lower()}{random_integers}{random_special_chars}", end='')
    i += 1
