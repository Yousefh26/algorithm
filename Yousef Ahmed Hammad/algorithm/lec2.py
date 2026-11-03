def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
def hybrid_sort(arr, left, right, k):
    if right - left + 1 <= k:
        insertion_sort(arr, left, right)
        return
    if left < right:
        mid = (left + right) // 2
        hybrid_sort(arr, left, mid, k)
        hybrid_sort(arr, mid + 1, right, k)
        left_copy = arr[left:mid + 1]
        right_copy = arr[mid + 1:right + 1]
        i = 0
        j = 0
        m = left
        while i < len(left_copy) and j < len(right_copy):
            if left_copy[i] <= right_copy[j]:
                arr[m] = left_copy[i]
                i = i + 1
            else:
                arr[m] = right_copy[j]
                j = j + 1
            m = m + 1
        while i < len(left_copy):
            arr[m] = left_copy[i]
            i = i + 1
            m = m + 1
        while j < len(right_copy):
            arr[m] = right_copy[j]
            j = j + 1
            m = m + 1