def counting_sort_naive(nums: list[int]):
    """计数排序"""
    # 简单实现，无法用于排序对象
    # 1. 统计数组最大元素 m
    m = max(nums)
    # 2. 统计各数字的出现次数
    # counter[num] 代表 num 的出现次数 counter索引即为 num
    counter = [0] * (m + 1)
    for num in nums:
        counter[num] += 1
    # 3. 遍历 counter ，将各元素填入原数组 nums
    i = 0
    for num in range(m + 1):
        # counter[num] 代表 num 的出现次数
        for _ in range(counter[num]):
            nums[i] = num
            i += 1

if __name__ == '__main__':
    nums = [1, 0, 1, 2, 0, 4, 0, 2, 2, 4]
    counting_sort_naive(nums)
    print(nums)