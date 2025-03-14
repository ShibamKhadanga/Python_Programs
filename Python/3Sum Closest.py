'''Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  
        l = len(nums)
        closest_sum = float('inf')

        for i in range(l - 2):
            left = i + 1
            right = l - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return target

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum 

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
