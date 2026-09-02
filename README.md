# Experiment 2.1 - Subsets

## Subject
CC-II (24CSP-339)

## Experiment
LeetCode Problem #78 - Subsets

## Aim
To generate all possible subsets (power set) of an array containing unique integers.

## Problem Statement
Given an integer array `nums` containing unique elements, return all possible subsets (the power set).

The result must not contain duplicate subsets, and the subsets may be returned in any order.

## Input
[1, 2, 3]

## Output
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

## Number of Subsets
For `n` elements, the number of subsets is `2^n`.

For `[1, 2, 3]`:

`2^3 = 8`

Therefore, the output contains 8 subsets.

---

# Approach 1: Iterative Approach - Bit Manipulation

## Core Idea

There are exactly `2^n` subsets.

We iterate through every bitmask from `0` to `2^n - 1`.

For each mask, if the `i-th` bit is set, `nums[i]` is included in the subset.

Each bitmask represents exactly one unique subset.

## Algorithm

1. Calculate the number of elements `n`.
2. Iterate from `0` to `2^n - 1`.
3. Create an empty subset.
4. Check each bit of the current mask.
5. If the `i-th` bit is set, add `nums[i]` to the subset.
6. Add the subset to the result.
7. Return all generated subsets.

## Implementation

The iterative implementation is available in:

`subsets_iterative.py`

## Complexity

**Time Complexity:** `O(n * 2^n)`

**Space Complexity:** `O(n * 2^n)`

---

# Approach 2: Recursive Approach - Backtracking

## Core Idea

The backtracking approach generates subsets by making include/exclude choices for each element.

At every step:

1. Record the current subset.
2. Choose an element.
3. Recursively generate subsets using the remaining elements.
4. Remove the last element to backtrack.
5. Continue until all possibilities are explored.

## Algorithm

1. Initialize an empty result list.
2. Define a backtracking function with a starting index and current subset.
3. Add a copy of the current subset to the result.
4. Iterate through the elements from the starting index.
5. Add the current element to the subset.
6. Recursively call the function with the next index.
7. Remove the last element to backtrack.
8. Return the result.

## Implementation

The backtracking implementation is available in:

`subsets.py`

## Complexity

**Time Complexity:** `O(n * 2^n)`

**Space Complexity:** `O(n * 2^n)`

---

# Test Cases

| Input | Number of Subsets |
|---|---:|
| `[1, 2, 3]` | 8 |
| `[0]` | 2 |
| `[1, 2]` | 4 |
| `[7]` | 2 |
| `[4, 5, 6, 7]` | 16 |

---

# Sample Output for [1, 2, 3]

## Backtracking

```text
Input: [1, 2, 3]
Subsets: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
Total number of subsets: 8