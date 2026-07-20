def knapsack():
    n = int (input ("Enter the number of items: "))
    weight = []
    value = []

    for c in range (n):
        w = int (input ("Enter the weight of items: "))
        weight.append (w)
    
    for i in range (n):
        v = int (input ("Enter the value of items: "))
        value.append (v)
    
    c = int (input ("Enter the capacity of knapsack: "))

    V = [[0 for _ in range(c + 1)] for i in range(n + 1)]
    
    for i in range (1, n+1):
        for c in range (1, c+1):
            if weight [i-1] <= c:

                if value [i-1] + V[i-1][c-weight[i-1]] > V[i-1][c]:
                    V[i][c] = value [i-1] + V[i-1][c-weight[i-1]]
                else:
                    V[i][c] = V[i-1][c]
            
            else:
                V[i][c] = V[i-1][c]

    print ("\nDP Table:")
    for row in V:
        print(row)
    
    print ("\nMaximum Value in knapsack =", V[n][c])

knapsack()