def insertion_sort(n):
    for i in range(1, len(n)):
        temp = n[i]
        j = i - 1

        while j >= 0 and n[j]>temp:
            n[j + 1] = n[j]
            j = j-1
        n[j+1] = temp
        
    return n

n = [19, 17, 7, 15, 6, 8]
print(insertion_sort(n))