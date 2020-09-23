def can_reach_end(arr):
    """
    input:     arr = [3, 3, 1, 0, 2, 0, 1]
    output:     True
    input:     arr = [3, 3, 1, 0, 2, 0, 0, 1]
    output:     False
    input:     arr = [3, 2, 0, 0, 2, 0, 1]
    output:     False

    Note: For each element, know the maximum index you can reach,
          and keep incrementing your "i" and check if you will have
          more maximum index as long as your "i" <= your current maximum index
          until reaching the end of the array or until it stop somewhere.

    Time Complexity: O(N)
    Space Complexity: O(1)

    """

    max_index = 0
    i = 0
    while i < len(arr) and i <= max_index:
        index = i + arr[i]
        max_index = index if index > max_index else max_index
        if max_index >= len(arr) -1:
            return True
        i += 1
    return False

def get_min_steps_to_reach_end(arr):
    """
    Page 45. Variant
    Write a program to compute the minimum number of steps needed to advance to the last location
    """
    pass


if __name__ == "__main__":
    arr = [3, 3, 1, 0, 2, 0, 1]
    print(can_reach_end(arr))
    arr = [3, 3, 1, 0, 2, 0, 0, 1]
    print(can_reach_end(arr))
    arr = [3, 2, 0, 0, 2, 0, 1]
    print(can_reach_end(arr))
    arr = [0, 0, 5, 1, 0, 0, 1, 0, 0]
    print(can_reach_end(arr))