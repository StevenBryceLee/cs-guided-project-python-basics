"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
def nth_smallest(lst, n):
    return sorted(lst)[n-1] if (n - 1) < len(lst) else None
    # Your code here


print(nth_smallest([7,3, 1], 1))
print(nth_smallest([1,5, 7], 3))
print(nth_smallest([1,5, 7], 5))
print(nth_smallest([7,5, 1], 2))