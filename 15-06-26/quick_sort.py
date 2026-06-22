def quick_sort(A, lb, ub):
    if lb < ub:
        loc = partition(A, lb, ub)
        quick_sort(A, lb, loc - 1)
        quick_sort(A, loc + 1, ub)

def partition(A, lb, ub):
    pivot = A[lb]
    i = lb + 1
    j = ub

    while i < j:
        while A[i] <= A[pivot]:
            i =+ 1
        while A[j] > A[pivot]:
            j =-1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            A[pivot], A[j] = A[j], A[pivot]

    return j

j = list(map(int, input("Enter numbers: ").split()))
print("Sorted Array: ", quick_sort(j, 0, len(j)-1))