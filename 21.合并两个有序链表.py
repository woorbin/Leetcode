#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        # 虚拟头指针
        # 当你需要创造一条新链表的时候，（如把两条有序链表合并成一条新的有序链表，把一条链表分解成两条链表）可以使用虚拟头结点简化边界情况的处理
        dummy=ListNode(-1)
        p=dummy
        p1=list1
        p2=list2      
        while p1 and p2:
            if p1.val<p2.val:
                p.next=p1
                p1=p1.next
            else:
                p.next=p2
                p2=p2.next
            # 指针不断前进
            p=p.next
        if p1:
            p.next=p1
        if p2:
            p.next=p2
        return dummy.next
# @lc code=end

