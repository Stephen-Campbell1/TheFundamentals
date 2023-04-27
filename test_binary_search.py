from typing import Callable, List
from binary_search import binary_search
import time
from multiprocessing import Pool, TimeoutError
import pytest

def test_binary_search_middle_index():
    # Arrange
    subject = [1,2,3,4]
    to_find = 3
    expected = 2
    
    # Act
    actual = binary_search(subject, to_find)

    # Assert
    assert actual == expected

def test_binary_search_beginning_index():
    # Arrange
    subject = [1,2,3,4]
    to_find = 1
    expected = 0

    # Act
    actual = binary_search(subject, to_find)

    # Assert
    assert actual == expected


def test_binary_search_end_index():
    # Arrange
    subject = [1,2,3,4]
    to_find = 4
    expected = 3

    # Act
    actual = binary_search(subject, to_find)

    # Assert
    assert actual == expected

def test_binary_search_missing():
    # Arrange
    subject = [1,2,3,4]
    to_find = 5
    expected = -1

    # Act
    actual = binary_search(subject, to_find)

    # Assert
    assert actual == expected


# Algorithmic Complexity Tests

# Because we are running a cpu bound operation, we create a separate process pool
# and run the operation from there, cancelling it if it surpasses the timeout
def timeout_test_util(func: Callable, timeout: float):
    with Pool(2) as p:
        result = p.apply_async(func)
        result.get(timeout=timeout)
        assert result.successful() == True

# Creating this input space has a time complexity O(n)
# so let's be sure to create it outside the test
huge_value = 50_000_000
heuristic_threshold_seconds = 1e-3
input_space = list(range(huge_value))

def bound_binary_search():
    found = binary_search(input_space, huge_value-1)
    assert found == huge_value - 1

# This is a heuristic test that asserts that the binary search is faster than
# some threshold. In this case, we are searching for an edge element (the worst
# case) in an array of 50,000,000 elements
def test_logrithmic_worst_case_complexity():
    timeout_test_util(bound_binary_search, heuristic_threshold_seconds)

        
def scan_search(nums: List[int], target: int) ->int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def bound_scan_search():
    found = scan_search(input_space, huge_value-1)
    assert found == huge_value - 1


## This is a meta-test that ensures that our above timeout heuristic will fail with an O(n) algo
def test_scan_search_fails_timeout_test():
    with pytest.raises(TimeoutError):
        timeout_test_util(bound_scan_search, heuristic_threshold_seconds)