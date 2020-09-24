def find_duplicate_element(arr):
    pass
def find_missed_element(arr):
    """
    Assuming you have Numbers from 1 to N=len(arr)=4 like [1, 2, 3, 4] but not neccessarily in sorted order, and one of the
    number either duplicated like [1, 2, 2, 3, 4] or missed like [1, 3, 4]. How would you figure out the duplicated
    or the missed number?
    Approach 1. Sorting Way: Sort the array, O(N log N), and loop through to find the duplicate or the missed, O(N).
                so, O(N log N) + O(N) => O(N log N)
            2. Mathematician Way: N(N+1)/2 will give as the sum of numbers from 1 upto N, then subtract from/to
                                  the sum of the actual ARRAY to get the duplicate OR the MISSED.
            3. XOR Way: Take the FULL array, [1, 2, 3, 4] and XOR it with the actual array, [1, 2, 2, 4] or
            [1, 3, 4]. Then every element in the array, except the duplicate or missed element, cancels out each
            other.
    """
    pass

def find_duplicate_and_missing_elements(arr):
    """
    Question: Here we have both scenarios i.e DUPLICATE AND MISSED like [1, 2, 2, 4]

    Approach 1. Brute-force: Have a Hash table or Dictionary to loop over the array and store the element. If the newly
                added element already exist, then it's DUPLICATED.
                At last, loop over the FULL array, [1, 2, 3, 4], and check if element exist in your Hash table as the
                non existed ones are the MISSED one.
                Time: O(N)
                Space: O(N)
             2. Sorting Way: After sorting, loop over the sorted array and identify the duplicated and missed easily
                Time: O(N log N)
                Space: O(1)
            3. XOR XOR on Page 159

    """
    pass