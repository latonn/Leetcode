# Time:  O(k * n^k)
# Space: O(k)

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find
# all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # latonn's
        dp = [[] for _ in range(target+1)]
        for num in candidates:
            if num <= target:
                dp[num].append([num])

        for i in range(target+1):
            if not dp[i]:
                continue
            for c in candidates:
                if not dp[i] or i + c > target or c > target + 1:
                    continue
                for j in range(len(dp[i])):
                    tmp = sorted(dp[i][j]+[c])
                    if not dp[i+c]:
                        dp[i+c] = [tmp]
                    elif tmp not in dp[i+c]:
                        dp[i+c].append(tmp)
                    del tmp
        return dp[target] if dp[target] else []

        # kamyu's
    #     result = []
    #     self.combinationSumRecu(sorted(candidates), result, 0, [], target)
    #     return result
    #
    # def combinationSumRecu(self, candidates, result, start, intermediate, target):
    #     if target == 0:
    #         result.append(list(intermediate))
    #     while start < len(candidates) and candidates[start] <= target:
    #         intermediate.append(candidates[start])
    #         self.combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
    #         intermediate.pop()
    #         start += 1


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
