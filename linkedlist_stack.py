from linked_list import ListNode


class LinkedListStack:
    """基于链表实现的栈"""
    def __init__(self):
        """初始化链表栈 头节点视为栈顶"""
        self.__head: ListNode | None = None
        self.__size: int = 0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.__size == 0

    def push(self, val: int) -> None:
        """入栈"""
        node = ListNode(val)
        node.next = self.__head
        self.__head = node
        self.__size += 1

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self.__head.val

    def pop(self) -> int:
        val = self.peek()
        self.__head = self.__head.next
        self.__size -= 1
        return val

    def to_list(self) -> list[int]:
        res = []
        node = self.__head
        while node:
            res.append(node.val)
            node = node.next
        res.reverse()
        return res


if __name__ == '__main__':
    stack = LinkedListStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.to_list())
    print(stack.peek())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.size())
    print(stack.peek())
    print(stack.to_list())