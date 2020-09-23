import heapq
def merge_sorted_arrays1(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))

def merge_sorted_arrays2(*sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == "__main__":
    sorted_arrays = [[3, 5, 7], [0, 6], [0, 6, 28]]
    result = merge_sorted_arrays1(sorted_arrays)
    print(result)
    a, b, c = [3, 5, 7], [0, 6], [0, 6, 28]
    result = merge_sorted_arrays2(a, b, c)
    print(result)

