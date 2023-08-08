'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.
For example, the message '111' would give 3, 
since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
'''

from collections import defaultdict


def solution_recursive(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1:
        return 1
    total = 0
    if int(s[:2]) <= 26:
        total += solution_recursive(s[2:])
    total += solution_recursive(s[1:])
    return total


def solution_dynamic(s):
    cache = defaultdict(int)
    cache[len(s)] = 1
    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]
    

tests = [
    {
        'incase': '111',
        'expect': 3,
    }
]


for i, test in enumerate(tests):
    incase = test['incase']
    expect = test['expect']
    result = solution_recursive(incase)
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
