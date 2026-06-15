def selection_sort(n):
    for i in range(len(n)):
        min_index = i

        for j in range(i + 1, len(n)):
            if n[j] < n[min_index]:
                min_index = j

        n[i], n[min_index] = n[min_index], n[i]

    return n

n = list(map(int, input("Enter integers separated by space: ").split()))

print("Sorted Array:", selection_sort(n)) 