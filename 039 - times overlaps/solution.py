def overlaps(a, b):
    start_a, end_a = a
    start_b, end_b = b
    return not (end_a < start_b or start_a > end_b)


def solution_naive(intervals):
    current_max = 0
    for interval in intervals:
        num_overlapping = sum(overlaps(interval, other_interval)
            for other_interval in intervals
            if interval is not other_interval)
        current_max = max(current_max, num_overlapping)
    return current_max


def solution_expert(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)

    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max


tests = [
    {
        'incase': [(30, 75), (0, 50), (60, 150)],
        'expect': 2
    }
]

for i, test in enumerate(tests):
    incase = test['incase']
    expect = test['expect']
    result = solution_expert(incase)
    if result == expect:
        print('Test', i, 'success!')
    else:
        print('Test', i, 'fail!!!')
        print('Expected:')
        print(expect)
        print('Resulted:')
        print(result)