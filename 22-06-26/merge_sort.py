def merge(A, lb, mid, ub): 
    i = lb
    j = mid + 1
    k = lb
    b = [0]*len(A)

    while i<=mid and j<=ub:
        if A[i] <= A[j]:
            b[k] = A[i]
            i+=1
            k+=1
        else:
            b[k] = A[j]
            j+=1
            k+=1
        if i>mid:
            while j<=ub:
                k+=1
                j+=1
        else:
            while i<=mid:
                b[k]= A[i]
                k+=1
                i+=1
    for k in range (lb, ub):
        A[k] = b[k]

def merge_sort(A, lb, ub):
    if lb<ub:
        mid = (lb+ub)//2
        merge_sort(A, lb, mid)
        merge_sort(A, mid+1, ub)
        merge(A, lb, mid, ub)

A = list(map(int, input("Enter numbers: ").split()))
print("Sorted Array: ", merge_sort(A, 0, len(A)-1)) 