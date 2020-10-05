# Star Question
def permutations_driver(arr):
    result = []
    collector = []
    return permutations(arr, result, collector)

def permutations(arr, result, collector):
    if len(arr) == 0:
        collector.append(result)

    i = 0
    while i < len(arr):
        permutations(arr[:i] + arr[i+1:], result + [arr[i]], collector)
        i += 1

    return collector

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    result = permutations_driver(arr)
    print(result)

