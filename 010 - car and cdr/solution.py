'''
Problem
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(c):
    def get(a, b):
        return a
    return c(get)

def cdr(c):
    def get(a, b):
        return b
    return c(get)

tests = [
    {
        'incase': cons(1, 2),
        'tester': car,
        'expect': 1,
    },
    {
        'incase': cons(1, 2),
        'tester': cdr,
        'expect': 2,
    },
]

for i, test in enumerate(tests):
    incase = test['incase']
    tester = test['tester']
    expect = test['expect']
    result = tester(incase)
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
