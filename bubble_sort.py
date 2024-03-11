import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def create_random_array(n, min_val, max_val):
    arr = []
    for _ in range(n):
        arr.append(random.randint(min_val, max_val))
    return arr

x = create_random_array(10000,1,20)
print("Before sorting: ",x)
start_time = time.perf_counter()
print("After sorting: ",bubble_sort(x))
end_time = time.perf_counter()
execution_time = end_time - start_time
print("Execution time: ","{:.20f}".format(execution_time))