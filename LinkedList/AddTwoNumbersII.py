# # Definition for singly-linked list.
# from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         num1 = 0
#         num2 = 0

#         while l1:
#             num1 = num1 * 10 + l1.val
#             l1 = l1.next

#         while l2:
#             num2 = num2 * 10 + l2.val
#             l2 = l2.next

#         num = num1 + num2
#         head = None

#         if num == 0:
#             return ListNode(0)

#         while num:
#             digit = num % 10
#             num = num // 10
#             node = ListNode(digit)
#             node.next = head
#             head = node

#         return head


# sol = Solution()
# print(sol.addTwoNumbers([7, 2, 4, 3], [5, 6, 4]))


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)

        total_sum = num1 + num2

        if total_sum == 0:
            return ListNode(0)

        # Convert the sum to a linked list representation
        dummy_head = ListNode()
        current_node = dummy_head

        while total_sum > 0:
            digit = total_sum % 10
            current_node.next = ListNode(digit)
            current_node = current_node.next
            total_sum //= 10

        return dummy_head.next

    def get_number(self, l: Optional[ListNode]) -> int:
        num = 0

        while l:
            num = num * 10 + l.val
            l = l.next

        return num


# Helper function to convert a list of digits to a ListNode
def create_linked_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head

    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


# Test the solution
sol = Solution()
# Convert the lists to ListNode instances
l1 = create_linked_list([7, 2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = sol.addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next
