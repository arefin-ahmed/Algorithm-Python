def knapsack(weight, value, n, w, V):
    n = int (input ("Enter the number of items: "))
    weight = []
    value = []

    for c in range (w):
        w = int (input ("Enter the weight of items: "))
        weight.append (w)
    
    for i in range (n):
        v = int (input ("Enter the value of items: "))
        value.append (v)
    
    for i in range (n):
        for c in range (w):
            if weight [i-1] <= c:

                if value [i-1] + V[i-1][c-weight[i-1]] > V[i-1][c]:
                    V[i][c] = value [i-1] + V[i-1][c-weight[i-1]]
                else:
                    V[i][c] = V[i-1][c]
            
            else:
                V[i][c] = V[i-1][c]
