def partition(nums: list[int], left: int, right: int) -> int:
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left

def partition_v2(nums: list[int], left: int, right: int) -> int:
    """哨兵划分"""
    # 以 nums[left] 作为基准数
    med = median_three(nums, left, (left + right) // 2, right)
    nums[left], nums[med] = nums[med], nums[left]
    i, j = left, right
    while i < j:
        # 从右向左找首个小于基准数的元素
        while i < j and nums[left] <= nums[j]:
            j -= 1
        # 从左向右找首个大于基准数的元素
        while i < j and nums[left] >= nums[i]:
            i += 1
        # 元素交换
        nums[i], nums[j] = nums[j], nums[i]
    # 将基准数交换至两子数组的分界线
    nums[i], nums[left] = nums[left], nums[i]
    return i

def median_three(nums: list[int], left: int, mid: int, right: int) -> int:
    """选取三个元素的中位数"""
    # 此处使用异或运算来简化代码
    # 异或规则为 0 ^ 0 = 1 ^ 1 = 0, 0 ^ 1 = 1 ^ 0 = 1
    if (nums[left] < nums[mid]) ^ (nums[left] < nums[right]):
        return left
    elif (nums[mid] < nums[left]) ^ (nums[mid] < nums[right]):
        return mid
    return right

def quick_sort(nums: list[int], left: int, right):
    if left < right:
        pivot = partition_v2(nums, left, right)
        quick_sort(nums, left, pivot - 1)
        quick_sort(nums, pivot + 1, right)

if __name__ == '__main__':
    nums = [1, 7, 6, 3, 2]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)