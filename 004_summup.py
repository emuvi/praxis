
def summup_naive(k, arr):
    for i1, a1 in enumerate(arr):
        for i2, a2 in enumerate(arr):
            if (i1 != i2 and a1 + a2 == k):
                return True
    return False

def summup_with_set(k, arr):
    seen = set()
    for a in arr:
        if k - a in seen:
            return True
        seen.add(a)
    return False

if __name__ == "__main__":
    cases = [
        (True, 17, [10, 15, 3, 7])
    ]
    for i, test in enumerate(cases):
        expected = test[0]
        k = test[1]
        arr = test[2]
        print("Executing test", i + 1)
        result = summup_with_set(k, arr)
        if result == expected:
            print("Ok")
        else:
            print("Fail", expected, result)
