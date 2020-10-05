# Star Question
def generate_power_set_iteratively(s):
    result = [[]]
    for e in s:
        newsubset = [subset + [e] for subset in result]
        result.extend(newsubset) # tricky: every loop we have different 'result'
    return result

def generate_power_set_recursively_driver(arr):
    result = [[]]
    return generate_power_set_recursively(arr, result)

def generate_power_set_recursively(arr, result):
    if not arr:
        return result
    e = arr[0]
    prev_result = result[:]
    for i in range(len(result)):
        result[i] = result[i] + [e]
    result.extend(prev_result)
    return generate_power_set_recursively(arr[1:], result)


if __name__ == "__main__":
    s = [1, 2, 3]
    r = generate_power_set_iteratively(s)
    print(r)

    arr = [1, 2, 3]
    p = generate_power_set_recursively_driver(arr)
    print(p)



