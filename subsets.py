class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])

                backtrack(i + 1, current)

                current.pop()

        backtrack(0, [])

        return result


# Test the program
nums = [1, 2, 3]

solution = Solution()

answer = solution.subsets(nums)

print("Input:", nums)
print("Subsets:", answer)
print("Total number of subsets:", len(answer))