def knapsack(weight, profit, W):
    n = len(weight)


    V = [[0 for c in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(W + 1):

            if weight[i - 1] <= c:            # Item can be part of the solution

                if profit[i - 1] + V[i - 1][c - weight[i - 1]] > V[i - 1][c]:
                    V[i][c] = profit[i - 1] + V[i - 1][c - weight[i - 1]]
                else:
                    V[i][c] = V[i - 1][c]

            else:                      # Item cannot be part of the solution
                V[i][c] = V[i - 1][c]

    print("\nKnapsack Table:")
    print("     ", end="")

    for c in range(W + 1):
        print(f"{c:5}", end="")
    print()

    for i in range(n + 1):
        print(f"{i:5}", end="")

        for c in range(W + 1):
            print(f"{V[i][c]:5}", end="")

        print()
 
    selected_items = []
    c = W

    for i in range(n, 0, -1):

        if V[i][c] != V[i - 1][c]:
            selected_items.append(i)
            c = c - weight[i - 1]

    selected_items.reverse()

    print("\nMaximum Total Profit:", V[n][W])

    print("Selected Items:", end=" ")

    for item in selected_items:
        print(f"Item {item}", end=" ")

    total_weight = sum(weight[i - 1] for i in selected_items)

    print("\nTotal Weight:", total_weight)


n = int(input("Enter the number of items: "))

weight = []
profit = []

for i in range(n):
    w = int(input(f"Enter the weight of Item {i + 1}: "))
    weight.append(w)

for i in range(n):
    p = int(input(f"Enter the profit of Item {i + 1}: "))
    profit.append(p)

W = int(input("Enter the capacity of the knapsack: "))

knapsack(weight, profit, W)