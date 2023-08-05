
from functools import reduce
from operator import mul


def solution_single_line(arr):
    return [reduce(mul, arr) / i for i in arr]


def solution_with_no_division(arr):
    prefixes = []
    for num in arr:
        if prefixes:
            prefixes.append(prefixes[-1] * num)
        else:
            prefixes.append(num)
    suffixes = []
    for num in reversed(arr):
        if suffixes:
            suffixes.append(suffixes[-1] * num)
        else:
            suffixes.append(num)
    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(suffixes[i + 1])
        elif i == len(arr) -1:
            result.append(prefixes[i - 1])
        else:
            result.append(prefixes[i - 1] * suffixes[i + 1])
    return result
    

if __name__ == "__main__":
    cases = [
        ([120, 60, 40, 30, 24], [1, 2, 3, 4, 5]),
        ([2, 3, 6], [3, 2, 1]),
    ]
    for i, test in enumerate(cases):
        expected = test[0]
        arr = test[1]
        print("Executing test", i + 1)
        result = solution_single_line(arr)
        if result == expected:
            print("Ok")
        else:
            print("Fail", expected, result)