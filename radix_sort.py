import random
import time

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def create_random_array(n, min_val, max_val):
    arr = []
    for _ in range(n):
        arr.append(random.randint(min_val, max_val))
    return arr

x = create_random_array(10000,1,20)
print("Before sorting: ",x)
start_time = time.perf_counter()
print("After sorting: ",radix_sort(x))
end_time = time.perf_counter()
execution_time = end_time - start_time
print("Execution time: ","{:.20f}".format(execution_time))