def fib(n: int) -> int:
    return n if n in {0, 1} else fib(n-1) + fib(n-2)

def my_sum(n: int) -> int:
    return 0 if n == 0 else n + my_sum(n-1)

if __name__ == '__main__':
    for i in range(11):
        print(fib(i), end=' ')
    print()
    print(my_sum(10))