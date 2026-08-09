def quick_sort(A, lb, ub):
    if lb < ub:
        loc = partition(A, lb, ub)
        quick_sort(A, lb, loc - 1)
        quick_sort(A, loc + 1, ub)

def partition(A, lb, ub):
    pivot = A[lb]
    i = lb + 1
    j = ub

    while i <= j:
        while i <= ub and A[i] <= pivot:
            i += 1
        while j <= ub and A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            A[lb], A[j] = A[j], A[lb]

    return j

A = list(map(int, input("Enter numbers: ").split()))
quick_sort(A, 0, len(A)-1)

print("Sorted Array: ", A)