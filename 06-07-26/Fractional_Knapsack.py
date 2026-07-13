profit = [0.0] * 100
weight = [0.0] * 100
itemFraction = [0.0] * 100

def knapsack(maxWeight, n):
    for i in range(n):
        MAX = i
        for j in range(i+1, n):
            if(profit[j]/weight[j] > profit[MAX]/weight[MAX]):
                MAX = j

        if MAX != i:
           profit[MAX], profit[i] = profit[i], profit[MAX]
           weight[MAX], weight[i] = weight[i], weight[MAX]

    capacity = maxWeight
  
    for i in range (n):
        if weight [i] > capacity:
            break
        itemFraction[i] = 1.0
        capacity -= weight[i]
    if i < n:
        itemFraction[i] = capacity / weight[i]

    # for i in range(n):
    # if weight[i] > capacity:
    #     itemFraction[i] = capacity / weight[i]
    #     break

    # itemFraction[i] = 1.0
    # capacity -= weight[i]

def profit_calculation (n):
    totalProfit = 0
    for i in range (n):
        totalProfit += itemFraction[i]*profit[i]
    # print(totalProfit)
    return totalProfit

n = int(input("Enter number of items: "))

for i in range(n):
    profit[i] = float(input(f"Profit of item {i+1}: "))

for i in range(n):
    weight[i] = float(input(f"Weight of item {i+1}: "))

maxWeight = float(input("Enter knapsack capacity: "))

knapsack(maxWeight, n)
print(f"Maximum Profit = {profit_calculation(n):.2f}")