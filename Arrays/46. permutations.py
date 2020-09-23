"""
Given a collection of distinct integers, return all possible permutations.
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

def permute(nums):
    nums2 = nums[:] # copying the nums to reserve
    start = 0
    result = []
    return permutation(nums, nums2, start, result)


def permutation(nums, nums2, start, result):

    if start == len(nums) - 1:
        print(nums)
        result.append(nums)

    for i in range(start, len(nums)):
        nums2 = nums[:]
        nums[i], nums[start] = nums[start], nums[i]
        permutation(nums, nums2, start + 1, result)
        nums = nums2[:] # bringing nums back to the original value, [1, 2, 3]
    return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(permute(nums))



