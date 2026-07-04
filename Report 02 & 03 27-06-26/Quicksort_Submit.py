import random
comparisons = 0
def partition(A, lb, ub):
    global comparisons

    random_pivot = random.randint(lb, ub)

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
