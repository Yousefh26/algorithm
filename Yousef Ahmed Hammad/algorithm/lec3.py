import heapq
def min_meeting(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort()
    heap = []
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    return len(heap)