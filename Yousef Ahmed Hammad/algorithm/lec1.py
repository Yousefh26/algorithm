import time
import random
def insertion_sort(arr):
    comparisons = 0
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons = comparisons + 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts = shifts + 1
                j = j - 1
            else:
                break
        arr[j + 1] = key
    return comparisons, shifts
sizes = [100, 500, 1000, 5000]
for n in sizes:
    random_arr = []
    for _ in range(n):
        random_arr.append(random.randint(1, 10000))
    start_time = time.time()
    insertion_sort(random_arr)
    end_time = time.time()
    time_taken = end_time - start_time
    print("Time for n =", n, time_taken, "seconds")