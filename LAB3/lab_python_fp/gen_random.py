import random

def gen_random(count, minimum, maximum):
    for i in range(count):
        yield random.randint(minimum, maximum)

for number in gen_random(5, 1, 3):
    print(number)