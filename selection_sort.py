import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def create_random_array(n, min_val, max_val):
    arr = []
    for _ in range(n):
        arr.append(random.randint(min_val, max_val))
    return arr

x = create_random_array(10000,1,20)
print("Before sorting: ",x)
start_time = time.perf_counter()
print("After sorting: ",selection_sort(x))
end_time = time.perf_counter()
execution_time = end_time - start_time
print("Execution time: ","{:.20f}".format(execution_time))