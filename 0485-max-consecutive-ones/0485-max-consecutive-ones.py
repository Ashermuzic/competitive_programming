class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mainCount = 0
        count = 0

        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
                
            mainCount = max(mainCount, count)
        return mainCount