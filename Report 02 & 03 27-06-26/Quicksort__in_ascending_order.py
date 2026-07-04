import random
comparisons = 0
def partition(A, lb, ub):
    global comparisons

    # Select a random pivot
    random_pivot = random.randint(lb, ub)

    # Swap random pivot with first element
    A[random_pivot], A[lb] = A[lb], A[random_pivot]

    pivot = lb
    i = lb
    j = ub

    while i < j:

        while i <= ub:
            comparisons += 1
            if A[i] <= A[pivot]:
                i += 1
            else:
                break

        while j >= lb:
            comparisons += 1
            if A[j] > A[pivot]:
                j -= 1
            else:
                break

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[pivot], A[j] = A[j], A[pivot]

    return j


def quick_sort(A, lb, ub):
    if lb < ub:
        location = partition(A, lb, ub)

        quick_sort(A, lb, location - 1)
        quick_sort(A, location + 1, ub)


# -------------------------------
# User Input
# -------------------------------

n = int(input("Enter array size: "))

A = []

print("Enter array elements:")

for _ in range(n):
    A.append(int(input()))

comparisons = 0

quick_sort(A, 0, len(A) - 1)

print("\nSorted Array (Ascending):")
print(A)

print("Number of Comparisons:", comparisons)


# --------------------------------
# Comparison Analysis
# --------------------------------

sizes = [100, 500, 1000, 5000]

comparison_counts = []

print("\nComparison Analysis")

for size in sizes:

    test = [random.randint(1, 100000) for _ in range(size)]

    comparisons = 0

    quick_sort(test, 0, len(test) - 1)

    comparison_counts.append(comparisons)

    print(f"n = {size:5d} --> Comparisons = {comparisons}")


# --------------------------------
# Plot Graph
# --------------------------------

plt.plot(sizes, comparison_counts, marker='o')

plt.title("Quick Sort Performance")

plt.xlabel("Input Size (n)")

plt.ylabel("Number of Comparisons")

plt.grid(True)

plt.show()