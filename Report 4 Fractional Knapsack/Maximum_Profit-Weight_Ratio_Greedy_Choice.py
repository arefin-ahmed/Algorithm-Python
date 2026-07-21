def fractional_knapsack_ratio(profit, weight, capacity):
    n = len(profit)

    # Create list of items
    items = []

    for i in range(n):
        ratio = profit[i] / weight[i]
        items.append([profit[i], weight[i], ratio])

    # Sort by profit/weight ratio in descending order
    for i in range(n):
        MAX = i

        for j in range(i + 1, n):
            if items[j][2] > items[MAX][2]:
                MAX = j

        if MAX != i:
            items[i], items[MAX] = items[MAX], items[i]

    total_profit = 0
    item_fraction = [0] * n

    # Select items
    for i in range(n):
        if items[i][1] <= capacity:
            item_fraction[i] = 1
            capacity = capacity - items[i][1]
            total_profit = total_profit + items[i][0]

        else:
            item_fraction[i] = capacity / items[i][1]
            total_profit = total_profit + (
                item_fraction[i] * items[i][0]
            )
            break

    return total_profit

# Input
profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

# Function call
result = fractional_knapsack_ratio(
    profit, weight, capacity
)

print("Profit/Weight Ratio Greedy")
print("Total Profit =", result)