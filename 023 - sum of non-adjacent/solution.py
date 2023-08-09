'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest 
sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def solution_recursive(arr):
    if not arr:
        return 0

    return max(
            solution_recursive(arr[1:]),
            arr[0] + solution_recursive(arr[2:]))


def solution_dynamic(arr):
    if len(arr) <= 2:
        return max(0, max(arr))
    cache = [0 for i in arr]
    cache[0] = max(0, arr[0])
    cache[1] = max(cache[0], arr[1])
    for i in range(2, len(arr)):
        num = arr[i]
        cache[i] = max(num + cache[i - 2], cache[i - 1])
    return cache[-1]


def solution_dynamic_improved(arr):
    if len(arr) <= 2:
        return max(0, max(arr))
    max_excluding_last= max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])
    for num in arr[2:]:
        prev_max_including_last = max_including_last
        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last
    return max(max_including_last, max_excluding_last)


tests = [
    {
        'incase': [2, 4, 6, 2, 5],
        'expect': 13,
    },
    {
        'incase': [5, 1, 1, 5],
        'expect': 10,
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