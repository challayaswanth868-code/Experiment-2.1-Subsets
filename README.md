# Experiment 2.1 - Subsets

## Subject
CC-II (24CSP-339)

## Experiment
LeetCode Problem #78 - Subsets

## Aim
To generate all possible subsets (power set) of an array containing unique integers using the backtracking technique.

## Problem Statement
Given an integer array nums containing unique elements, return all possible subsets (the power set).

The result must not contain duplicate subsets, and the subsets may be returned in any order.

## Algorithm
1. Initialize an empty result list.
2. Define a backtracking function with a starting index and current subset.
3. Add a copy of the current subset to the result.
4. Iterate through the elements from the starting index.
5. Add the current element to the subset.
6. Recursively generate subsets using the next index.
7. Remove the last element to backtrack.
8. Return the result.

## Input
[1, 2, 3]

## Output
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

## Number of Subsets
8

## Complexity Analysis
Time Complexity: O(n * 2^n)

Space Complexity: O(n * 2^n)

## Result
Thus, all possible subsets of the given array were successfully generated using the backtracking technique.