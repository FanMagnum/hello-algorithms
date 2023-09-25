def bubble_sort(nums: list[int]):
    """冒泡排序"""
    for i in range(len(nums) - 1):
        flag = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            break

if __name__ == '__main__':
    nums = [1, 7, 6, 3, 2]
    bubble_sort(nums)
    print(nums)