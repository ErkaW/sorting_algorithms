import random
import time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def create_random_array(n, min_val, max_val):
    arr = []
    for _ in range(n):
        arr.append(random.randint(min_val, max_val))
    return arr

x = create_random_array(10000,1,20)
print("Before sorting: ",x)
start_time = time.perf_counter()
print("After sorting: ",insertion_sort(x))
end_time = time.perf_counter()
execution_time = end_time - start_time
print("Execution time: ","{:.20f}".format(execution_time))