def knapsack(weight, profit, W):
    n = len(weight)

    # Create the DP table
    V = [[0 for c in range(W + 1)] for i in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for c in range(W + 1):

            if weight[i - 1] <= c:
                # Item can be included
                if profit[i - 1] + V[i - 1][c - weight[i - 1]] > V[i - 1][c]:
                    V[i][c] = profit[i - 1] + V[i - 1][c - weight[i - 1]]
                else:
                    V[i][c] = V[i - 1][c]

            else:
                # Item cannot be included
                V[i][c] = V[i - 1][c]

    # Display the whole table
    print("Knapsack Table:")
    print("     ", end="")

    for c in range(W + 1):
        print(f"{c:5}", end="")
    print()

    for i in range(n + 1):
        print(f"{i:5}", end="")
        for c in range(W + 1):
            print(f"{V[i][c]:5}", end="")
        print()

    # Find selected items
    selected_items = []
    c = W

    for i in range(n, 0, -1):
        if V[i][c] != V[i - 1][c]:
            selected_items.append(i)
            c = c - weight[i - 1]

    selected_items.reverse()

    # Display result
    print("\nMaximum Total Profit:", V[n][W])

    print("Selected Items:", end=" ")
    for item in selected_items:
        print(f"Item {item}", end=" ")

    print()

    total_weight = sum(weight[i - 1] for i in selected_items)
    print("Total Weight:", total_weight)


# Input
weight = [2, 1, 3, 2]
profit = [12, 10, 20, 15]
W = 5

# Run the algorithm
knapsack(weight, profit, W)