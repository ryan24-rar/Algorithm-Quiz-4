class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0

        for i in range(len(nums)):
            total += nums[i]
        
        if total % 2 != 0:
            return False

        target = total // 2
        possible = {0}

        for num in nums:
            new_possible = set(possible)

            for s in possible:
                new_possible.add(s + num)

            possible = new_possible

            if target in possible:
                return True

        return target in possible
