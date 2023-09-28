# Python Program to implement merge sort using
# multi-threading
import threading
import time
import random

# number of elements in array
MAX = 100000

# number of threads
THREAD_MAX = 4

array = [0] * MAX


def merge_sort(result,array):
    if len(array) <= 1:
        result = array
        return result

    # Divide the array into two halves.
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Create a multiprocessing pool.
    # Submit each sublist to the pool for sorting.
    tmp1 = list()
    tmp2 = list()
    results = [merge_sort(tmp1,left), merge_sort(tmp2,right)]

    # Wait for all of the sublists to be sorted.

    # Merge the sorted sublists together.
    for i in merge(results[0],results[1]):
      result.append(i)

    return result
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left list to the result.
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right list to the result.
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# thread function for multi-threading
def merge_sort_threaded(array):
  part = 0
  result = [[],[],[],[]]
  # creating 4 threads
  t = [[],[],[],[]]
  for i in range(THREAD_MAX):
    t[i] = threading.Thread(target=merge_sort, args=(result[part], array[((part*MAX)//THREAD_MAX) :((part+1)*(MAX))//THREAD_MAX]))
    part += 1
  for i in range(THREAD_MAX):
    t[i].start()

  # joining all 4 threads
  for i in range(THREAD_MAX):
    t[i].join()

  # merge 4 array cuoi cung
  # print(result)
  ret1 = merge(result[0], result[1])
  ret2 = merge(result[2], result[3])
  return merge(ret1,ret2)

# Driver Code
# generating random values in array
random.seed(2)
totaltime = [0,0]
for i in range(MAX):
  array[i] = random.randint(0, 1000000)

# merge sort using multithread
result = []
t1 = time.perf_counter()
result = merge_sort_threaded(array)
t2 = time.perf_counter()
totaltime[0] += t2-t1
#merge sort
result = []
t1 = time.perf_counter()
merge_sort(result, array)
t2 = time.perf_counter()
totaltime[1] += t2-t1

print(f"Average time taken using multithread: {totaltime[0]:.6f} seconds")

result = []
print(f"Average time taken: {totaltime[1]:.6f} seconds")
