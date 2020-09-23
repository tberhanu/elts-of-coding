def phone_mnemonic(nums):
    """
    Time Complexity: O(4**N)(N)
    Since the tree has at most 4 branches i.e 4**1, 4**2, 4**3 ... 4**N
    And each base case make a copy string and add to the result which takes O(N). Therefore, O(4**N)(N)
    """
    lst = []
    collector = []
    return phone_mnemonic_helper(nums, lst, collector)
def phone_mnemonic_helper(nums, lst, collector):
    MAPPING = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")
    if len(nums) == 0:
        collector += lst
        return

    letters = MAPPING[int(nums[0])]
    lst2 = []
    for letter in letters:
        if len(lst) == 0:
            lst2.append(letter)
        else:
            for i in range(len(lst)):
                e = lst[i] + letter
                lst2.append(e)
    phone_mnemonic_helper(nums[1:], lst2, collector)

    return collector

if __name__ == "__main__":
    print(phone_mnemonic("29"))
    print(phone_mnemonic("234"))