def insertion_sort(nums: list[int]):
    """插入排序"""
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break

def insertion_sort_v2(nums: list[int]):
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = base

if __name__ == '__main__':
    nums = [1, 7, 6, 3, 2]
    insertion_sort_v2(nums)
    print(nums)