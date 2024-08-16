class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rem_val = {}

        for indx, val in enumerate(nums):
            rem = target - val

            if rem in rem_val:
                rem_indx = rem_val[rem]
                return [indx, rem_indx]

            rem_val[val] = indx

        return None


arr1 = [4, 6, 5, 2, 1]
target = 8
sol = Solution()
output = sol.twoSum(arr1, target)
print(output)
