def insertion_sort(n):
    for i in range(1, len(n)):
        temp = n[i]
        j = i - 1

        while j >= 0 and n[j] < temp:
            n[j + 1] = n[j]
            j = j - 1

        n[j + 1] = temp

    return n


n = input("Enter characters separated by space: ").split()
print("Sorted Array:", insertion_sort(n))