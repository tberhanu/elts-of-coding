def decompose_into_dictionary_words(str, dictionary):
    N = len(str)
    cache = create_the_cache_table(N)
    for length in range(N):
        for start in range(N):
            # START and END always differ by LENGTH, w/c is the length of the substring we deal with
            end = start + length
            if end >= N:
                break
            concatenated_found = False
            substring = str[start: end + 1] # 'end + 1' since string slicing not inclusive of the 'end'
            if substring in dictionary:
                cache[start][end] = True # just 'end' since our cache is defined as inclusive of the 'end'
                continue
            for k in range(start, end):
                if cache[start][k] and cache[k + 1][end]:
                    cache[start][end] = True
                    concatenated_found = True
                    break
            if not concatenated_found:
                cache[start][end] = False
    print(cache)
    return cache[0][N - 1]

def create_the_cache_table(N):

    cache = [[0 for _ in range(N)] for _ in range(N)]
    return cache


if __name__ == "__main__":
    dictionary = {"a", "I", "am", "ace"} # Assuming "mace" is not in the dictionary
    str = "Iamace"
    result = decompose_into_dictionary_words(str, dictionary)
    print(result) # True
    # Here's the last state of our cache.
    # [[True, True, True, True, False, True],
    #  [0   , True, True, True, False, True],
    #  [0   , 0   , False, False, False, False],
    #  [0   , 0   , 0    , True, False, True],
    #  [0   , 0   , 0    , 0   , False, False],
    #  [0   , 0   , 0    , 0   , 0    , False]]
