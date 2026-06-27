def merge(A, lb, mid, ub):
    i = lb
    j = mid + 1
    k = lb
    b = [0] * len(A)

    while i <= mid and j <= ub:
        if A[i] <= A[j]:
            b[k] = A[i]
            i += 1
        else:
            b[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        b[k] = A[i]
        i += 1
        k += 1

    while j <= ub:
        b[k] = A[j]
        j += 1
        k += 1

    for idx in range(lb, ub + 1):
        A[idx] = b[idx]


def merge_sort(A, lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2
        merge_sort(A, lb, mid)
        merge_sort(A, mid + 1, ub)
        merge(A, lb, mid, ub)


if __name__ == "__main__":
    A = list(map(int, input("Enter numbers: ").split()))
    merge_sort(A, 0, len(A) - 1)
    print("Sorted Array:", A)