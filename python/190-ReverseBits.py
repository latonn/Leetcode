#

# Reverse bits of a given 32 bits unsigned integer.
#
# Example:
#
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
#              return 964176192 represented in binary as 00111001011110000010100101000000.
# Follow up:
# If this function is called many times, how would you optimize it?


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            digit = int(n%2)
            n = int(n/2)
            ans = ans * 2 + digit
            # print(n, ans)
        return ans


if __name__ == '__main__':
    input = 43261596
    print(Solution().reverseBits(input))
