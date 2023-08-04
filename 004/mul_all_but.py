
from functools import reduce
from operator import mul


def single_line(arr):
    return [reduce(mul, arr) / i for i in arr]


def no_division(arr):
    pass


if __name__ == "__main__":
    cases = [
        ([120, 60, 40, 30, 24], [1, 2, 3, 4, 5]),
        ([2, 3, 6], [3, 2, 1]),
    ]
    for i, test in enumerate(cases):
        expected = test[0]
        arr = test[1]
        print("Executing test", i + 1)
        result = single_line(arr)
        if result == expected:
            print("Ok")
        else:
            print("Fail", expected, result)