# Password Cracker
import string
import itertools
import time as t

password = input("Please insert your password: ")
letters = string.ascii_lowercase


def guesser(password):
    trials = 0
    for x in range(1, 9):
        for y in itertools.product(letters, repeat=x):
            trials += 1
            y = ''.join(y)
            if y == password:
                return [y, trials]


start = t.time()
result = guesser(password)
end = t.time()


print(f"The password is {result[0]} and it came out after {result[1]} trials after {end - start} seconds")
