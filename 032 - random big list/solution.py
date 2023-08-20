import random

def pick(big_stream):
    random_element = None
    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

class Generator():
    def __init__(self):
        self.item = 0

    def __iter__(self):
        while self.item < 1000000:
            self.item += 1
            yield self.item

print(pick(Generator()))