def fractional_knapsack_profit(profit, weight, capacity):
    n = len(profit)
    items = []
    for i in range(n):
        items.append([profit[i], weight[i]])

    for i in range(n):
        MAX = i
        
        for j in range(i + 1, n):
            if items[j][0] > items[MAX][0]:
                MAX = j

        if MAX != i:
            items[i], items[MAX] = items[MAX], items[i]

    total_profit = 0
    item_fraction = [0] * n

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


profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

result = fractional_knapsack_profit(
    profit, weight, capacity
)

print("Maximum Profit Greedy")
print("Total Profit =", result)