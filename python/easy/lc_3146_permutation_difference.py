class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        final_sum: int = 0

        for i in range (len(s)):
            final_sum += abs(i - t.index(s[i]))
        return final_sum
