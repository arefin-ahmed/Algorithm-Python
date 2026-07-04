def partition(A, lb, ub):

    pivot_index = int(input(f"Enter pivot index ({lb} to {ub}): "))

    while pivot_index < lb or pivot_index > ub:
        pivot_index = int(input("Invalid index. Enter again: "))

    # Move selected pivot to the first position
    A[pivot_index], A[lb] = A[lb], A[pivot_index]

    pivot = lb
    i = lb
    j = ub

    while i < j:

        while i <= ub and A[i] <= A[pivot]:
            i += 1

        while A[j] > A[pivot]:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[pivot], A[j] = A[j], A[pivot]

    return j


def quick_sort(A, lb, ub):

    if lb < ub:

        location = partition(A, lb, ub)

        quick_sort(A, lb, location - 1)

        quick_sort(A, location + 1, ub)


# Main Program

n = int(input("Enter array size: "))

A = []

print("Enter array elements:")

for _ in range(n):
    A.append(int(input()))

quick_sort(A, 0, n - 1)

print("\nSorted Array (Ascending):")
print(A)