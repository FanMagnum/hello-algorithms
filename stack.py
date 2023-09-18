# 初始化栈
# python没有内置的栈类，可以把list当作栈来使用
stack: list[int] = []

# 元素入栈
stack.append(1)
stack.append(2)

# 访问栈顶元素
peek: int = stack[-1]
print(peek)

# 元素出栈
pop: int = stack.pop()

# 判断栈是否为空
is_empty: bool = not stack
print(is_empty)

# 获取栈的长度
size: int = len(stack)