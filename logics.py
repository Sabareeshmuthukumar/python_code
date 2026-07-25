"""
Top Python Logical & Algorithmic Interview Problems
====================================================
A curated collection of top coding interview problems frequently asked in technical interviews.
Includes clean Python implementations, explanations, complexity analysis, and runnable test assertions.
"""

from typing import List, Dict, Tuple, Optional


# ==============================================================================
# SECTION 1: ARRAYS & TWO POINTERS
# ==============================================================================

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    1. TWO SUM
    --------------------------------------------------------------------------
    Problem: Find indices of two numbers in `nums` such that they add up to `target`.
    Approach: Hash Map storing compliment (target - num) -> index.
    Time Complexity: O(n) | Space Complexity: O(n)
    """
    seen: Dict[int, int] = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []


def max_sub_array(nums: List[int]) -> int:
    """
    2. KADANE'S ALGORITHM (Maximum Subarray Sum)
    --------------------------------------------------------------------------
    Problem: Find contiguous subarray with the largest sum.
    Approach: Track running current_max. Decide whether to extend running sum or restart.
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    max_so_far = nums[0]
    current_max = nums[0]
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far


def container_with_most_water(height: List[int]) -> int:
    """
    3. CONTAINER WITH MOST WATER
    --------------------------------------------------------------------------
    Problem: Find two vertical lines that form container holding maximum water.
    Approach: Two Pointers starting at extremities. Move shorter line inward.
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        current_water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


def move_zeroes(nums: List[int]) -> None:
    """
    4. MOVE ZEROES IN-PLACE
    --------------------------------------------------------------------------
    Problem: Move all 0s to the end of array while keeping relative order of non-zero elements.
    Approach: Two pointers (`write_idx` and iterator).
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    write_idx = 0
    for read_idx in range(len(nums)):
        if nums[read_idx] != 0:
            nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
            write_idx += 1


# ==============================================================================
# SECTION 2: STRINGS & SLIDING WINDOW
# ==============================================================================

def is_palindrome(s: str) -> bool:
    """
    5. VALID PALINDROME
    --------------------------------------------------------------------------
    Problem: Check if string is palindrome considering only alphanumeric characters and ignoring case.
    Approach: Two pointers filtering alphanumeric characters.
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def length_of_longest_substring(s: str) -> int:
    """
    6. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
    --------------------------------------------------------------------------
    Problem: Find length of longest substring without repeating characters.
    Approach: Sliding Window with Hash Map recording last seen index of characters.
    Time Complexity: O(n) | Space Complexity: O(min(n, m))
    """
    char_map: Dict[str, int] = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    7. GROUP ANAGRAMS
    --------------------------------------------------------------------------
    Problem: Group strings that are anagrams of each other.
    Approach: Hash map where key is sorted string or character count tuple.
    Time Complexity: O(n * k log k) | Space Complexity: O(n * k)
    """
    anagram_map: Dict[str, List[str]] = {}
    for word in strs:
        sorted_key = "".join(sorted(word))
        if sorted_key not in anagram_map:
            anagram_map[sorted_key] = []
        anagram_map[sorted_key].append(word)
    return list(anagram_map.values())


# ==============================================================================
# SECTION 3: MATH, BITWISE & LOGIC PUZZLES
# ==============================================================================

def single_number(nums: List[int]) -> int:
    """
    8. SINGLE NUMBER (Bitwise XOR Trick)
    --------------------------------------------------------------------------
    Problem: All elements appear twice except one. Find the single element.
    Approach: XOR all numbers together. Since A ^ A = 0 and A ^ 0 = A, duplicates cancel.
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    res = 0
    for num in nums:
        res ^= num
    return res


def missing_number(nums: List[int]) -> int:
    """
    9. MISSING NUMBER IN RANGE [0..n]
    --------------------------------------------------------------------------
    Problem: Given array containing `n` distinct numbers in range `0..n`, find missing one.
    Approach: Gauss summation formula `expected_sum = n * (n + 1) // 2`.
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


def fibonacci(n: int) -> int:
    """
    10. FIBONACCI NUMBER (Iterative Space-Optimized)
    --------------------------------------------------------------------------
    Problem: Compute N-th Fibonacci number.
    Approach: Iterative bottom-up state swap storing only last two numbers.
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ==============================================================================
# SECTION 4: STACKS & DYNAMIC PROGRAMMING
# ==============================================================================

def is_valid_parentheses(s: str) -> bool:
    """
    11. VALID PARENTHESES
    --------------------------------------------------------------------------
    Problem: Determine if input string has valid matching parentheses '()[]{}'.
    Approach: Stack tracking open brackets.
    Time Complexity: O(n) | Space Complexity: O(n)
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map:
            top = stack.pop() if stack else '#'
            if bracket_map[char] != top:
                return False
        else:
            stack.append(char)
    return not stack


def product_except_self(nums: List[int]) -> List[int]:
    """
    12. PRODUCT OF ARRAY EXCEPT SELF
    --------------------------------------------------------------------------
    Problem: Return array where output[i] is product of all elements except nums[i]. No division allowed.
    Approach: Two passes computing running prefix and suffix products.
    Time Complexity: O(n) | Space Complexity: O(1) extra space
    """
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


# ==============================================================================
# RUNNABLE VERIFICATION SUITE
# ==============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print(" Running Verification Tests for Python Interview Problems ")
    print("=" * 60)

    # 1. Two Sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    print("[OK] 1. Two Sum: Passed")

    # 2. Kadane's Algorithm
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("[OK] 2. Kadane's Algorithm: Passed")

    # 3. Container With Most Water
    assert container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print("[OK] 3. Container With Most Water: Passed")

    # 4. Move Zeroes
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    assert arr == [1, 3, 12, 0, 0]
    print("[OK] 4. Move Zeroes: Passed")

    # 5. Valid Palindrome
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    print("[OK] 5. Valid Palindrome: Passed")

    # 6. Longest Substring Without Repeating Chars
    assert length_of_longest_substring("abcabcbb") == 3
    print("[OK] 6. Longest Substring: Passed")

    # 7. Group Anagrams
    grouped = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(grouped) == 3
    print("[OK] 7. Group Anagrams: Passed")

    # 8. Single Number
    assert single_number([4, 1, 2, 1, 2]) == 4
    print("[OK] 8. Single Number: Passed")

    # 9. Missing Number
    assert missing_number([3, 0, 1]) == 2
    print("[OK] 9. Missing Number: Passed")

    # 10. Fibonacci
    assert fibonacci(10) == 55
    print("[OK] 10. Fibonacci: Passed")

    # 11. Valid Parentheses
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    print("[OK] 11. Valid Parentheses: Passed")

    # 12. Product Except Self
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    print("[OK] 12. Product Except Self: Passed")

    print("\nAll 12 Interview Logical Problems Executed and Verified Successfully!")
