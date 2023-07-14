TODO:
(**DAY1**)[https://labuladong.github.io/algo/zhun-bei-g-8db77/pei-tao-vs-de2a8/]  
# update  
(**7.14____21.合并两个有序链表**)[https://github.com/woorbin/Leetcode/blob/master/21.合并两个有序链表.py]  
(**7.14____86.分隔链表**)[https://github.com/woorbin/Leetcode/blob/master/7.14____86.分隔链表.py]  
# Notes  
21.合并有序列表  
当你需要创造一条新链表的时候，（如把两条有序链表合并成一条新的有序链表，把一条链表分解成两条链表）可以使用虚拟头结点简化边界情况的处理。dummy=ListNode(-1) p=dummy  
86.分隔链表  
把原链表分成两个小链表，一个链表中的元素大小都小于 x，另一个链表中的元素都大于等于 x，最后再把这两条链表接到一起。
23.合并-k-個升序链表  
难点：快速得到k个节点中的最小节点  
解决：优先级队列（二叉堆） 把链表节点放进一个最小堆，就可以每次获得k个节点中的最小节点  
    # 优先级队列，最小堆  
    pq = []  
    for head in lists:  
        if head:  
            heapq.heappush(pq, (head.val, head))  

    while pq:  
        # 获取最小节点，接到结果链表中  
        node = heapq.heappop(pq)[1]  
        p.next = node  
        if node.next:  
            heapq.heappush(pq, (node.next.val, node.next))  
            