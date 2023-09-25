def selection_sort(nums: list[int]):
    """选择排序"""
    # 外循环：未排序区间为 [i, n-1]
    for i in range(len(nums) - 1):
        min_index = i
        # 内循环：找到未排序区间内的最小元素
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

if __name__ == '__main__':
    nums = [1, 7, 6, 3, 2]
    selection_sort(nums)
    print(nums)