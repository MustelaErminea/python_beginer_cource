# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        step: int = 1
        result: int = 0
        node = ListNode()

        while l1 is not None or l2 is not None:
            if l1 is not None:
                result = result + l1.val * step

            if l2 is not None:
                result = result + l2.val * step

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

            step = step * 10

            node.val = int(result / step)
            node.next = ListNode()
            node = node.next

        print(f"Result: {result}")
        return node


def fill_nodes(values: List[int]) -> ListNode:
    values.reverse()

    list_node: ListNode = None
    prev: ListNode = None

    for num in values:
        list_node = ListNode(num, prev)
        prev = list_node

    return list_node


def main():
    solution: Solution = Solution()

    l1: ListNode = fill_nodes([9, 9, 9, 9, 9, 9, 9])
    l2: ListNode = fill_nodes([9, 9, 9, 9])

    node: ListNode = solution.add_two_numbers(l1, l2)
    print(f"Result: {node.val}")


if __name__ == "__main__":
    main()
