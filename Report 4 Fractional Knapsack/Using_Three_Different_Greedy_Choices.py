def knapsack(profit, weight, capacity, choice):
    n = len(profit)

    for i in range(n):
        MAX = i

        for j in range(i + 1, n):

            if choice == 1:
                # Maximum Profit
                if profit[j] > profit[MAX]:
                    MAX = j

            elif choice == 2:
                # Minimum Weight
                if weight[j] < weight[MAX]:
                    MAX = j

            else:
                # P/W Ratio
                if profit[j] / weight[j] > profit[MAX] / weight[MAX]:
                    MAX = j

        profit[i], profit[MAX] = profit[MAX], profit[i]
        weight[i], weight[MAX] = weight[MAX], weight[i]

    total_profit = 0

    for i in range(n):

        if weight[i] <= capacity:
            capacity = capacity - weight[i]
            total_profit = total_profit + profit[i]

        else:
            fraction = capacity / weight[i]
            total_profit = total_profit + fraction * profit[i]
            break

    return total_profit


profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50


result1 = knapsack(profit.copy(), weight.copy(), capacity, 1)
result2 = knapsack(profit.copy(), weight.copy(), capacity, 2)
result3 = knapsack(profit.copy(), weight.copy(), capacity, 3)


print("Maximum Profit       :", result1)
print("Minimum Weight       :", result2)
print("Profit/Weight Ratio  :", result3)