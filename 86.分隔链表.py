#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) : #-> ListNode:
        # 存放小于x的链表的虚拟头结点
        dummy1=ListNode(-1)
        p1=dummy1
        dummy2=ListNode(-1)
        p2=dummy2
        p = head
        while p:
            if p.val>=x:
                p2.next=p
                p2=p2.next
            else:
                p1.next=p
                p1=p1.next
            # 断开原链表中的每个节点的next指针
            temp=p.next
            p.next=None
            p=temp
            # 连接两个链表
            p1.next=dummy2.next
            return dummy1.next

# @lc code=end

