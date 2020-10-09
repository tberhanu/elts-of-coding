from collections import Counter
def get_score_combination_driver(N):
    result = []
    collector = []
    return get_score_combination(N, result, collector)

def get_score_combination(N, result, collector):
    """
    Tess Strategy:
        Just did it with common recursion concept, and not sure where the DP is used.
        Check page 247

    """
    if N == 0:
        counts = Counter(result)
        if counts not in collector: # if we don't care about the ORDER OF THE SCORES, otherwise remove this line.
            collector.append(counts)
    elif N < 2:
        return
    else:
        get_score_combination(N - 2, result + ["safety(=2)"], collector)
        get_score_combination(N - 3, result + ["field goal(=3)"], collector)
        get_score_combination(N - 7, result + ["touchdown(=7)"], collector)


    return collector


if __name__ == "__main__":
    N = 12
    result = get_score_combination_driver(N)
    print(result)
