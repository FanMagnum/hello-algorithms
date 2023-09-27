def insertion_sort(nums: list[int]):
    """插入排序"""
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break

def insertion_sort_v2(nums: list[int]):
    """插入排序"""
    # 外循环：已排序区间为 [0, i-1]
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        # 内循环：将 base 插入到已排序区间 [0, i-1] 中的正确位置
        while j >= 0 and nums[j] > base:
            # 将 nums[j] 向右移动一位
            nums[j + 1] = nums[j]
            j -= 1
        # 将 base 赋值到正确位置
        nums[j + 1] = base

def test(nums: list[int]):
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        for j in range(i - 1, -1, -1):
            if nums[j] > base:
                nums[j + 1] = nums[j]
            else:
                break
        nums[j + 1] = base

if __name__ == '__main__':
    nums = [1, 7, 6, 3, 2]
    insertion_sort_v2(nums)
    print(nums)