def insertion_sort_desc(n):
    for i in range(1, len(n)):
        temp = n[i]
        j = i - 1
        while j >= 0 and n[j] < temp:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = temp
    return n


def main():
    user_input = input("Enter characters separated by spaces: ").split()
    sorted_chars = insertion_sort_desc(user_input)
    print("Sorted characters in descending order:", sorted_chars)


if __name__ == "__main__":
    main()
