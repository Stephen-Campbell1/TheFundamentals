from typing import List

# https://leetcode.com/problems/binary-search/
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def binary_search(nums: List[int], target: int) ->int:
    # High Level Idea
    # Because the array is ordered, If you look at any one element, all elements to the left
    # are guaranteed to be smaller and all elements to the right are guarantted to be larger
    # To maximize the amount of elements we can eliminate, we can look at the middle element.
    # This guarantees we will (at the very least) eliminate half of the elements from contention

    # Preconditions
    assert len(nums) > 0

    # Let's find the half way point
    # This can be tricky because the middle point for collections with even elements 
    # is not well defined. At the end of the day, all we care about is getting eliminating  
    # half the candiates from contention and a 1 element overestimation is not very costly. 
    # The only thing to remember is to be consistent with how the middle element is chosen when
    # there is an even amount of elements in contention
    left_bound_inclusive = 0
    right_bound_exclusive = len(nums)

    while(True):
        # Let's check if we've eliminated all possibilites and return the flag
        if right_bound_exclusive - left_bound_inclusive == 0:
            return -1

        # We use integer division to pick the middle element using the above bounds
        # This decision picks the middle element for odd collections and the left middle element for even collections
        # [ 0, 1, 2, 3, 4 ] :  Odd Numbered Collection
        #         ^  -  - ^   -> middle element is 3
        # [ 0, 1, 2, 3, 4] :  Odd Numbered Collection
        #   ^  -  ^         -> middle element is 0
        middle_index = (right_bound_exclusive - left_bound_inclusive) // 2 + left_bound_inclusive
        found = nums[middle_index]

        # Let's see if our guess matches the target
        if found == target:
            return middle_index

        # Since we did'nt find the target, Let's adjust our bounds to reflect
        # which elements we can eliminate from contention
        if target > found:
            left_bound_inclusive = middle_index + 1
        elif target < found:
            right_bound_exclusive = middle_index