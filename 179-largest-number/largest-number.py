class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):  # i -> index & n -> value
            nums[i] = str(n)         # change the values to str

        def compare(a, b):          # custom compare function to use it in the sorted function as key function
            if a + b > b + a:       # 330 or 303
                return -1           # return the 1st one == a
            else:
                return 1           # return the 2nd one == b

        nums = sorted(nums, key=cmp_to_key(compare))  #sorts it in the nums list.

        return str(int("".join(nums))) # When [0, 0, 0] output should be => only 0 not "000"

        


