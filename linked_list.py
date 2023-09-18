from typing import Optional


class ListNode:
    def __repr__(self) -> str:
        return str(self.val)

    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[ListNode] = None

def insert(node:ListNode, new: ListNode):
    """在链表的节点 node 之后插入节点 new"""
    n1 = node.next
    node.next = new
    new.next = n1

def remove(node: ListNode):
    """删除链表的节点 node 之后的首个节点"""
    if node.next:
        after = node.next
        n1 = after.next
        node.next = n1

def access(head: ListNode, index: int) -> ListNode | None:
    """访问链表中索引为 index 的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

def traverse(head: ListNode):
    """遍历链表"""
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")

def find(head: ListNode, target: int) -> int:
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

if __name__ == '__main__':
    # 初始化链表 1 -> 3 -> 2 -> 5 -> 4
    # 初始化各个节点
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(5)
    node5 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    traverse(node1)
    insert(node2, ListNode(6))
    traverse(node1)
    remove(node3)
    traverse(node1)
    print(find(node1, 6))
    print(access(node1, 2))
