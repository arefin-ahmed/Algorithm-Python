def fractional_knapsack_min_weight(profit, weight, capacity):
    n = len(profit)

    # Create list of items
    items = []

    for i in range(n):
        items.append([profit[i], weight[i]])

    # Sort by weight in ascending order
    for i in range(n):
        MIN = i

        for j in range(i + 1, n):
            if items[j][1] < items[MIN][1]:
                MIN = j

        if MIN != i:
            items[i], items[MIN] = items[MIN], items[i]

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
result = fractional_knapsack_min_weight(
    profit, weight, capacity
)

print("Minimum Weight Greedy")
print("Total Profit =", result)