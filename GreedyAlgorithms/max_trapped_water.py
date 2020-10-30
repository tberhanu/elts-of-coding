def max_trapped_water(heights):
    """
    An array of integers naturally defines a set of lines parallel to the Y-axis, starting from X = 0. Your task is
    to find the pair of lines that together with the X-axis "trap" the MOST WATER.

    Question: Write a program which takes as input an integer array and returns the pair of entries that trap the
              maximum amount of water.

    Strategy 1: Brute-force: Double for loop: O(N * N)
    Strategy 2: Divide and Conquer: max water can be trapped by the left half, right half or across the center.
                T(n) = T(n/2) + T(n/2) + O(N**2 / 4) since even if we keep divide the problem by half, we still need
                to perform sth similar to the brute-force when we left with three indices or two intervals, so
                will end up in Time: O(N * N) w/c is similar to the Brute-force.
    Strategy 3:
            i) Have two pointers at the start and end indices, and calculate the total water it can trap.
            ii) Then decrement/increment the indices of the shorter height and update the max water if any.
            Time: O(N)
            Space: O(1)
            Is this OPTIMAL ALL THE TIME? (MY QUESTION)
    """
    max_water = 0
    i, j = 0, len(heights) - 1
    indices = (i, j)
    while i < j:
        width = j - i
        curr_water_content = width * min(heights[i], heights[j])
        if curr_water_content > max_water:
            max_water = curr_water_content
            indices = (i, j)
        if heights[i] < heights[j]: # gives sense because the width is always constant, 1 unit
            i += 1
        else:
            j -= 1

    return max_water, indices

def maxArea(height):
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            left_height = height[i]
            right_height = height[j]
            h = min(left_height, right_height)
            width = j - i
            area = h * width
            if area > max_area:
                max_area = area
            if left_height <= right_height:
                i += 1
            else:
                j -= 1
        return max_area

if __name__ == "__main__":
    heights = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
    max_water, indices = max_trapped_water(heights)
    print("max water: ", max_water)
    print("start index: ", indices[0])
    print("end index: ", indices[1])

    h = [1, 1]
    a = maxArea(h)
    print(a)
