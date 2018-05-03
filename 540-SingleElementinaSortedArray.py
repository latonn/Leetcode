# Time:  O(logn)
# Space: O(1)

# Given a sorted array consisting of only integers where every element
# appears twice except for one element which appears once. Find this
# single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
#
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
#
# Note: Your solution should run in O(log n) time and O(1) space.


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # latonn's
        mid = len(nums) // 2
        parity = mid % 2

        if len(nums) == 1:
            return nums[0]

        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        elif nums[mid] == nums[mid-1]:
            return self.singleNonDuplicate(nums[mid+1:]) if parity else self.singleNonDuplicate(nums[:mid-1])
        else:
            return self.singleNonDuplicate(nums[:mid]) if parity else self.singleNonDuplicate(nums[mid+2:])

        # kamyu's
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     mid = left + (right - left) / 2
        #     if not (mid%2 == 0 and mid+1 < len(nums) and \
        #             nums[mid] == nums[mid+1]) and \
        #        not (mid%2 == 1 and nums[mid] == nums[mid-1]):
        #         right = mid-1
        #     else:
        #         left = mid+1
        # return nums[left]


if __name__ == '__main__':
    # nums = [3, 3, 7, 7, 10, 11, 11]
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6]
    print(Solution().singleNonDuplicate(nums))

