# https://leetcode.com/problems/add-two-numbers/
import util


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    @staticmethod
    def toLinkedList(nums):
        root = ListNode(nums[0])
        node = root
        for x in nums[1:]:
            node.next = ListNode(x)
            node = node.next
        return root

    @staticmethod
    def toList(node):
        nums = [node.val]
        while node.next is not None:
            nums.append(node.next.val)
            node = node.next
        return nums

    @staticmethod
    def equals(a,b):
        return ListNode.toList(a) == ListNode.toList(b)


def addTwoNumbers(l1,l2):
    root = l1
    remainder = 0
    l1_prev = None
    while l1 is not None or l2 is not None:
        if l1 is None:
            l1_prev.next = l2
            l1 = l2
            l2 = None
        elif l2 is None:
            l1.val += remainder
            remainder = l1.val//10
            l1.val %= 10
            if remainder == 0:
                break
            l1_prev = l1
            l1 = l1.next
        else:
            l1.val += l2.val + remainder
            remainder = l1.val//10
            l1.val %= 10
            l1_prev = l1
            l1 = l1.next
            l2 = l2.next
    if remainder != 0 and l1_prev is not None:
        l1_prev.next = ListNode(remainder)
    return root


if __name__ == "__main__":
    solutions = [addTwoNumbers]
    tests = [
        (([2,4,3],[5,6,4]),[7,0,8]),
        (([0],[0]),[0]),
        (([9,9,9,9,9,9,9],[9,9,9,9]),[8,9,9,9,0,0,0,1]),
        (([2,4,9],[5,6,4,9]),[7,0,4,0,1])
    ]
    for i,(inputs,expected) in enumerate(tests):
        inputs = tuple(ListNode.toLinkedList(x) for x in inputs)
        expected = ListNode.toLinkedList(expected)
        tests[i] = (inputs,expected)
    util.run_tests(solutions,tests,equals=ListNode.equals)