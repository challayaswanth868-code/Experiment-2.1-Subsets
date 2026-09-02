class Solution:
    def subsets(self, nums):
        result = []

        n = len(nums)

        for mask in range(0, 2 ** n):
            subset = []

            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            result.append(subset)

        return result


# Test the program
nums = [1, 2, 3]

solution = Solution()

answer = solution.subsets(nums)

print("Input:", nums)
print("Subsets:", answer)
print("Total number of subsets:", len(answer))