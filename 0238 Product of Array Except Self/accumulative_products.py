"""
P: 1, 2, 3, 4 -> Result: 24, 12, 8, 6

L: 1, 2, 6, 24
R: 24, 24, 12, 4

P1: R2
P2: L1 * R3
P3: L2 * R4
P4: L3
"""

from typing import List


class Solution:
    @staticmethod
    def product_except_self(nums: List[int]) -> List[int]:
        left = []
        prev = 1

        for idx in range(len(nums)):
            left.append(nums[idx] * prev)
            prev = left[idx]

        right = nums.copy()
        prev = 1

        for idx in range(1, len(nums) + 1):
            right[-1 * idx] = nums[-1 * idx] * prev
            prev = right[-1 * idx]

        products = []

        for idx in range(len(nums)):
            lidx = idx - 1
            ridx = idx + 1

            if lidx == -1:
                products.append(right[ridx])

            elif ridx == len(nums):
                products.append(left[lidx])

            else:
                products.append(left[lidx] * right[ridx])

        return products
