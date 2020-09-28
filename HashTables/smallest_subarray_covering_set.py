def find_smallest_sequentially_covering_subset(paragraph, keywords):
    """
    # def find_smallest_subarray_covering_set(paragraph, keywords):
        pass
    paragraph = ["apple", "banana", "apple", "apple", "dog", "cat", "apple", "dog", "banana", "apple", "cat", "dog"]
    keywords = {"banana", "cat"}
    Brute-force: may take double for loop, O(N), plus O(n) to check if subarray covered .... >>> O(N * N * n)
    Tess Strategy:
        1. Traverse through the PARAGRAPH until reaching a point where KEYWORDS covered for the first time, and save
            the END index, j. This means the first subarray is from index i = 0 to END index, j.

        2. Increment i += 1, and check if still the resulting subarray covered, and if "Yes", keep incrementing i
           until you say "No" or until len(subarray) == len(keywords) in which case we are DONE.

        3. Once you say "No", then keep i as it is, and increment j += 1 until you reach the resulting subarray
           covered, and save the END index, j. Then do same thing like step 2.

    Tess Time Complexity: O(N) in the worst case
    Tess Space Complexity:O(1)

    NOTE: This code was for page 171 question(section 12.7) which is just to discover shortest cover of keywords in
          the paragraph which is relatively easy. But then a follow up Question on page 174(section 12.8) asks not only
          just the cover but also need to KEEP the ORDER, and the code updated likewise.
    """
    i = 0
    j = len(keywords)
    index_i = 0
    index_j = len(paragraph)
    shortest = index_j - index_i
    while j <= len(paragraph):
        subarray = paragraph[i:j]
        if is_keywords_in_subarray(keywords, subarray):
            if len(keywords) == len(subarray):
                return ("start: ", i, "end: ", j - 1) # j - 1 because j is not inclusive in subarray end index
            diff = j - i
            if diff < shortest:
                shortest = diff
                index_i = i
                index_j = j
            i += 1
        else:
            j += 1

    return ("start: ", index_i, "end: ", index_j - 1) # j - 1 because j is not inclusive in subarray end index

def is_keywords_in_subarray(keywords, subarray):
    i = 0
    k = 0
    # keywords = list(keywords)
    while i < len(subarray):
        if subarray[i] == keywords[k]:
            i += 1
            k += 1
            if k == len(keywords):
                return True
        else:
            i += 1
    return False
    # return keywords <= set(subarray)

if __name__ == "__main__":

    paragraph = ["apple", "banana", "apple", "apple", "dog", "cat", "apple", "dog", "banana", "apple", "cat", "dog"]
    keywords = ["banana", "cat"]
    result = find_smallest_sequentially_covering_subset(paragraph, keywords)
    print("1: ", result) # (8, 10)

    paragraph = ["apple", "banana", "apple", "apple", "dog", "cat", "apple", "dog", "banana", "apple", "dog"]
    keywords = ["banana", "dog"]
    result = find_smallest_sequentially_covering_subset(paragraph, keywords)
    print("2: ", result)  # (8, 10)

    paragraph = ["apple", "banana", "apple", "apple", "dog", "cat", "apple", "dog", "banana", "apple", "cat", "dog"]
    keywords = ["dog"]
    result = find_smallest_sequentially_covering_subset(paragraph, keywords)
    print("3: ", result) # (4, 4)

    paragraph = ["apple", "apple", "dog", "cat", "apple", "dogs", "banana", "apple", "cat", "ok", "dog"]
    keywords = ["cat", "dog"]
    result = find_smallest_sequentially_covering_subset(paragraph, keywords)
    print("4: ", result) # (8, 10)

    paragraph = ["apple", "banana", "dog", "apple", "dog", "cat", "apple", "dog", "banana", "apple", "cat", "dog"]
    keywords = ["dog", "apple", "banana"]
    result = find_smallest_sequentially_covering_subset(paragraph, keywords)
    print("5: ", result) # (4, 8)