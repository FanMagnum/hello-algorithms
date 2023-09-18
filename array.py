import random


def random_access(nums: list[int]) -> int:
    """随机访问元素"""
    random_index: int = random.randint(0, len(nums) - 1)
    return nums[random_index]

def insert(nums: list[int], num: int, index: int):
    """在数组的索引 index 处插入元素 num"""
    # 把索引 index 以及之后的所有元素向后移动一位，末尾元素将丢失
    for i in range(len(nums)-1, index, -1):
        nums[i] = nums[i-1]
    nums[index] = num

def remove(nums: list[int], index: int):
    """删除索引为 index 的元素, 原先末尾的元素变得“无意义”了"""
    for i in range(index, len(nums)-1):
        nums[i] = nums[i+1]

def traverse(nums: list[int]):
    """遍历数组"""
    for i in range(len(nums)):
        print(nums[i])
    for num in nums:
        print(num)
    for i, num in enumerate(nums):
        print(i, num)

def find(nums: list[int], target: int) -> int:
    """在数组中查找指定元素"""
    return next((i for i, num in enumerate(nums) if num == target), -1)

def exists(nums: list[int], enlarge: int) -> list[int]:
    """扩展数组长度"""
    # 初始化一个扩展长度后的数组
    res: list[int] = [0] * (len(nums) + enlarge)
    for i, num in enumerate(nums):
        res[i] = num
    return res

if __name__ == '__main__':
    # 初始化数组
    nums: list[int] = [1, 2, 3, 4, 5]
    print(random_access(nums))
    insert(nums, 5, 1)
    print(nums)
    remove(nums, 1)
    print(nums)
    traverse(nums)
    print(find(nums, 1))
    print(exists(nums, 2))