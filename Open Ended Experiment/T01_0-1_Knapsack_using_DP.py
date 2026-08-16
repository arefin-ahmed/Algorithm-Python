def knapsack(weight, profit, W):

    n = len(weight)


    V = [[0 for c in range(W + 1)] for i in range(n + 1)]


    for i in range(1, n + 1):

        for c in range(W + 1):

            if weight[i - 1] <= c:

                if profit[i - 1] + V[i - 1][c - weight[i - 1]] > V[i - 1][c]:

                    V[i][c] = profit[i - 1] + V[i - 1][c - weight[i - 1]]

                else:

                    V[i][c] = V[i - 1][c]

            else:

                V[i][c] = V[i - 1][c]

    print("\nDP Table:")

    names = ["None", "S1", "S2", "S3", "S4", "S5", "S6"]

    for start in range(0, W + 1, 10):

        end = min(start + 9, W)

        print("\nCapacity:", end=" ")

        for c in range(start, end + 1):
            print(f"{c:8}", end="")

        print()

        for i in range(n + 1):

            print(f"{names[i]:6}", end="")

            for c in range(start, end + 1):
                print(f"{V[i][c]:8}", end="")

            print()

    selected_sponsors = []

    c = W

    for i in range(n, 0, -1):

        if V[i][c] != V[i - 1][c]:

            selected_sponsors.append(i)

            c = c - weight[i - 1]

    selected_sponsors.reverse()


    print("\nMaximum Sponsorship:", V[n][W])

    print("Selected Sponsors:", end=" ")

    for i in selected_sponsors:
        print("S" + str(i), end=" ")

    print()

    total_space = 0

    for i in selected_sponsors:
        total_space = total_space + weight[i - 1]

    print("Total Space Used:", total_space, "sq.m")



sponsors = ["S1", "S2", "S3", "S4", "S5", "S6"]

weight = [10, 20, 15, 8, 12, 5]

profit = [60000, 100000, 120000, 50000, 70000, 30000]

W = 50



knapsack(weight, profit, W)


