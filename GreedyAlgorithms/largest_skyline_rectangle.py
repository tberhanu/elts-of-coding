# Exceptional !!!
def calculate_largest_rectangle(heights):
    """
    Given a sequence of adjacent buildings. Each has unit width and an integer height. These buildings from the skyline
    of a city. An architect wants to know the area of a largest rectangle contained in this skyline.
    Question:
        Let A be an array representing the heights of adjacent buildings of unit width. Design an algorithm to compute
        teh area of the largest rectangle contained in the skyline.

    Strategy: Smart usage of one Single Stack
        Remember: Don't even think about SORTING, as the nature of the problem doesn't allow you to do so.

    Time: O(N)
    Space: O(N)

    Note: Also check the book's solution @page 281.
    """
    i = 1
    stack_of_indices = [0]
    max_area = 0
    start_index, end_index = 0, 0
    while i < len(heights):
        curr_height = heights[i]
        prev_height = heights[stack_of_indices[-1]]
        if curr_height > prev_height: # should be > or >= ???? Looks both OK, but IMO, > is more efficient
            stack_of_indices.append(i)
        else:
            while stack_of_indices and curr_height < heights[stack_of_indices[-1]]:
                index = stack_of_indices.pop()
                height = heights[index]
                if len(stack_of_indices) == 0:
                    width = i
                else:
                    next_index_from_stack = stack_of_indices[-1]
                    width = i - next_index_from_stack - 1
                area = height * width
                if area > max_area:
                    max_area = area
                    if stack_of_indices:
                        start_index = stack_of_indices[-1] + 1
                    else:
                        start_index = 0
                    end_index = i - 1
            stack_of_indices.append(i)
        i += 1

    if stack_of_indices:
        # Remember index i = len(heights)
        while stack_of_indices:
            index = stack_of_indices.pop()
            height = heights[index]
            if len(stack_of_indices) == 0:
                width = i
            else:
                next_index_from_stack = stack_of_indices[-1]
                width = i - next_index_from_stack - 1
            area = height * width
            if area > max_area:
                max_area = area
                if stack_of_indices:
                    start_index = stack_of_indices[-1] + 1
                else:
                    start_index = 0
                end_index = i - 1

    return max_area, start_index, end_index


if __name__ == "__main__":
    heights = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
    area, start_index, end_index = calculate_largest_rectangle(heights)
    print("area: ", area) # 20 is OK
    print("start index: ", start_index) # 0 is NOT OK, should be 1     ???????
    print("end index: ", end_index) # 10 is OK