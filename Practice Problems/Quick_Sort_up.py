def quick_sort(A, lb, ub):
    if lb < ub:
        loc = partition(A, lb, ub)
        quick_sort(A, lb, loc - 1)
        quick_sort(A, loc + 1, ub)


def partition(A, lb, ub):
    pivot = A[ub]
    i = lb - 1
    j = lb

    while j < ub:
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

        j += 1

    A[i + 1], A[ub] = A[ub], A[i + 1]

    return i + 1


A = list(map(int, input("Enter numbers: ").split()))
quick_sort(A, 0, len(A) - 1)

print("Sorted Array: ", A)
