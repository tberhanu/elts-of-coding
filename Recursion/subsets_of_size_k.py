def get_all_subsets_of_size_k_driver(arr, k):
    result = [[]]
    return get_all_subsets_of_size_k(arr, k, result)

def get_all_subsets_of_size_k(arr, k, result):
    if not arr:
        return result
    e = arr[0]
    prev_result = result[:]
    for i in range(len(result)):
        r = result[i] + [e]
        if len(r) <= k:
            result[i] = r
        else:
            del prev_result[i] # to avoid redundant set w/c resulting by skipping longer than k items
    result.extend(prev_result)
    return get_all_subsets_of_size_k(arr[1:], k, result)

if __name__ == "__main__":
    # arr = [1, 2, 3]
    # r = get_all_subsets_of_size_k_driver(arr, 3)
    # print(r)
    arr = [1, 2, 3, 4]
    r = get_all_subsets_of_size_k_driver(arr, 2)
    print(r)