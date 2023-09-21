from linked_list import ListNode


class LinkedListQueue:
    def __init__(self):
        self.__front: ListNode | None = None
        self.__rear: ListNode | None = None
        self.__size: int = 0

    def size(self):
        return self.__size

    def is_empty(self) -> bool:
        return not self.__front

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        return self.__front.val

    def push(self, val: int):
        """入队"""
        # 尾节点后添加 num
        node = ListNode(val)
        # 如果队列为空，则令头、尾节点都指向该节点
        if self.__front is None:
            self.__front = node
        else:
            self.__rear.next = node
        self.__rear = node
        self.__size += 1

    def pop(self) -> int:
        res = self.peek()
        self.__front = self.__front.next
        self.__size -= 1
        return res

    def to_list(self) -> list[int]:
        res = []
        temp = self.__front
        while temp:
            res.append(temp.val)
            temp = temp.next
        return res

if __name__ == '__main__':
    queue = LinkedListQueue()
    queue.push(1)
    queue.push(2)
    print(queue.to_list())
    print(queue.peek())
    queue.pop()
    print(queue.to_list())
    print(queue.peek())