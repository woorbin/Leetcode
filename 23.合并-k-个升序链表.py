#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# from typing import List
import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        # 优先级队列，最小堆,存储元组，堆的顺序是根据 head.val 的值来确定的。较小的 head.val 值具有较高的优先级。
        pq = []
        for head in lists:
            if head:    
                heapq.heappush(pq, (head.val, head))   
                print(head.val)
        while pq:
            # 获取最小节点，接到结果链表中
            # heapq.heappop(pq) 用于从堆（优先队列）中弹出堆顶元素（元组）
            node = heapq.heappop(pq)[1]    
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            # p 指针不断前进
            p = p.next
        return dummy.next  
               
# @lc code=end

