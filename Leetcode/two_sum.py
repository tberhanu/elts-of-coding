def two_sum(nums, target):
    for i in range(len(nums)):
        arr = nums[:i] + nums[i+1:]
        num1 = nums[i]
        num2 = target - num1
        if num2 in arr:
            index = nums.index(num2)
            return (i, index)
    return (-1, -1)
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

    nums = [2, 7, 11, 15, 20]
    target = 31
    print(two_sum(nums, target))

    nums = [2, 7, 11, 15]
    target = 99
    print(two_sum(nums, target))