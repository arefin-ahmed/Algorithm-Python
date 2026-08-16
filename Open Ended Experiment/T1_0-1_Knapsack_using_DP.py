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
    print("Knapsack DP Table:")

    print("     ", end="")
    for c in range(W + 1):
        print(f"{c:6}", end="")
    print()

    for i in range(n + 1):
        print(f"{i:5}", end="")

        for c in range(W + 1):
            print(f"{V[i][c]:6}", end="")

        print()

    # Find selected sponsors
    selected_sponsors = []
    c = W

    for i in range(n, 0, -1):

        if V[i][c] != V[i - 1][c]:
            selected_sponsors.append(i)
            c = c - weight[i - 1]

    selected_sponsors.reverse()

    # Display result
    print("\nMaximum Sponsorship:", V[n][W])

    print("Selected Sponsors:", end=" ")

    for sponsor in selected_sponsors:
        print(f"S{ sponsor }", end=" ")

    print()

    total_space = sum(weight[i - 1] for i in selected_sponsors)

    print("Total Space Used:", total_space, "sq.m")


# Input
sponsors = ["S1", "S2", "S3", "S4", "S5", "S6"]

weight = [10, 20, 15, 8, 12, 5]

profit = [60000, 100000, 120000, 50000, 70000, 30000]

W = 50


# Run the algorithm
knapsack(weight, profit, W)