import heapq


def top_k_heap(nums: list[int], k: int) -> list[int]:
    """基于堆查找数组中最大的 k 个元素"""
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap


if __name__ == '__main__':
    nums = [1, 7, 6, 3, 2]
    print(top_k_heap(nums, 3))
