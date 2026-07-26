# Simple Version of 0/1 Knapsack Problem using Dynamic Programming
# Take input
n = int(input("Enter number of items: "))

weight = []
profit = []

for i in range(n):
    w = int(input("Enter weight of item " + str(i + 1) + ": "))
    weight.append(w)

for i in range(n):
    p = int(input("Enter profit of item " + str(i + 1) + ": "))
    profit.append(p)

W = int(input("Enter knapsack capacity: ")) 

# Create Knapsack Table
V = [[0 for c in range(W + 1)] for i in range(n + 1)]

# Fill the table
for i in range(1, n + 1):
    for c in range(W + 1):

        if weight[i - 1] <= c:

            if profit[i - 1] + V[i - 1][c - weight[i - 1]] > V[i - 1][c]:
                V[i][c] = profit[i - 1] + V[i - 1][c - weight[i - 1]]
            else:
                V[i][c] = V[i - 1][c]

        else:
            V[i][c] = V[i - 1][c]


# Display the Knapsack Table
print("\nKnapsack Table:")

for i in range(n + 1):
    print(V[i])

# Display maximum profit
print("\nMaximum Total Profit:", V[n][W])

# Find selected items
c = W
selected = []

for i in range(n, 0, -1):

    if V[i][c] != V[i - 1][c]:
        selected.append(i)
        c = c - weight[i - 1]

# Display selected items
selected.reverse()

print("Selected Items:", selected)