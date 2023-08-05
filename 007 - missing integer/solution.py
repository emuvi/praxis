'''
Problem
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer 
in linear time and constant space. In other words, find the lowest positive 
integer that does not exist in the array. The array can contain duplicates 
and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''


def solution_single_swap(case):
    if not case:
        return 1
    for i in range(len(case)):
        while i + 1 != case[i] and 0 < case[i] <= len(case):
            v = case[i]
            case[i], case[v - 1] = case[v - 1], case[i]
            if case[i] == case[v - 1]:
                break
    for i, num in enumerate(case, 1):
        if num != i:
            return i
    return len(case) + 1


def solution_with_set(case):
    s = set(case)
    i = 1
    while i in s:
        i += 1
    return i
    

tests = [
    {
        'incase': [3, 4, -1, 1],
        'expect': 2,
    },
    {
        'incase': [1, 2, 0],
        'expect': 3,
    }
]

for i, test in enumerate(tests):
    incase = test['incase']
    expect = test['expect']
    result = solution_with_set(incase)
    if expect == result:
        print('Test', i, 'success!');
    else:
        print('Test', i, 'fail!!!');
        print('InCase:');
        print(incase);
        print('Expect:');
        print(expect);
        print('Result:');
        print(result);
