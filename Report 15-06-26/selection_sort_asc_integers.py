# Task 2: Selection Sort on user-defined integers in ascending order

def selection_sort_asc(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


def main():
    user_input = list(map(int, input("Enter integers separated by spaces: ").split()))
    sorted_numbers = selection_sort_asc(user_input)
    print("Sorted integers in ascending order:", sorted_numbers)


if __name__ == "__main__":
    main()
