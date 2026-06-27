import random
import time
# import matplotlib.pyplot as plt

def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] >= right_part[j]:   # Descending
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


n = int(input("Enter array size: "))

arr = []

print("Enter elements:")

for i in range(n):
    arr.append(int(input()))

merge_sort(arr, 0, n - 1)

print("\nSorted Array (Descending):")
print(arr)


sizes = [100, 500, 1000, 5000]

times = []

for size in sizes:

    test = [random.randint(1, 100000) for _ in range(size)]

    start = time.perf_counter()

    merge_sort(test, 0, len(test) - 1)

    end = time.perf_counter()

    times.append(end - start)

print("\nExecution Time")

for s, t in zip(sizes, times):
    print(f"n = {s:5d} --> {t:.6f} seconds")

# plt.plot(sizes, times, marker='o')


# plt.title("Merge Sort Performance")

# plt.xlabel("Input Size (n)")

# plt.ylabel("Execution Time (seconds)")

# plt.grid(True)

# plt.show()