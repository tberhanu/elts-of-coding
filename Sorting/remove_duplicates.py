# Star Question
def remove_duplicates(arr):
    """
    Given an array, how do you remove duplicates IN-PLACE, O(1)
    """
    arr.sort() # Sort it first
    index = 1
    for elt in arr[1:]:
        if elt != arr[index - 1]: # continue until you get the UNIQUE elt.
            arr[index] = elt
            index += 1
    return arr[:index] # at last, return only up to our index using which we insert UNIQUE elts.

arr = [1, 2, 5, 5, 6, 2, 3, 1, 4, 4]
print(remove_duplicates(arr))