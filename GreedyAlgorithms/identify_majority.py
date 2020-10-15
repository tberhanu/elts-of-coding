def majority_search(input_stream):
    """
    Several applications require identification of elements in a sequence which occur more than a specified fraction of
    total number of elements in the sequence. For ex. we may wnat to identify the users using excessive network
    bandwidth or IP Addresses originating the most HTTP requests.

    Question: Write a program that makes a single pass over the sequence and identifies the majority element. For
              example, input: [b, a, c, a, a, b, a, a, c, a]
                       output: 'a'  since it appears 6 out of the 10 places

    Definition: Majority iff M/N > 1/2 where M is the count the candidate for majority, and N=len(input)

    Strategy 1: Hashtable, Counter: Time: O(N) Space: O(N)
    Strategy 2: Randomized Sampling can be used to identify a majority element with high probability using storage,
                but is not exact.
    Strategy 3:
        i) Initialize the first element as a candidate for being the majority, and iterate through the remaining array.
        ii) Each time we see entry equal to the candidate, we increment the count.
        iii) If entry is d/t, we decrement the count.
        iv) If the count reaches 0, we set the next element as a new candidate for the majority, and a count to be 1.
        v) ASSUMING the array has a MAJORITY, the last candidate with some positive count is the majority.

        Note: If the array not guaranteed to have a majority, then need to iterate once more to count our candidate
              to check if it is the majority.

        Time: O(N)
        Space: O(1)

    """
    candidate, candidate_count = None, 0
    for it in input_stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return  candidate

if __name__ == "__main__":
    input_stream = [6, 1, 6, 6, 4, 6,  6, 1, 6, 1, 1]
    result = majority_search(input_stream)
    print(result)
    input_stream = ['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a']
    result = majority_search(input_stream)
    print(result)