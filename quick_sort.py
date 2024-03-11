import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
def create_random_array(n, min_val, max_val):
    arr = []
    for _ in range(n):
        arr.append(random.randint(min_val, max_val))
    return arr

x = create_random_array(10000,1,20)
print("Before sorting: ",x)
start_time = time.perf_counter()
print("After sorting: ",quick_sort(x))
end_time = time.perf_counter()
execution_time = end_time - start_time
print("Execution time: ","{:.20f}".format(execution_time))