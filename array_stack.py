class ArrayStack:
    def __init__(self):
        self.__stack: list[int] = []

    def size(self) -> int:
        return len(self.__stack)

    def is_empty(self) -> bool:
        return not self.__stack

    def push(self, val: int) -> None:
        self.__stack.append(val)

    def pop(self) -> int:
        return self.__stack.pop()

    def peek(self) -> int:
        return self.__stack[-1]

    def to_list(self) -> list[int]:
        return self.__stack

if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(5)
    stack.push(7)
    stack.push(6)
    print(stack.to_list())
    print(stack.peek())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.size())
    print(stack.peek())
    print(stack.to_list())