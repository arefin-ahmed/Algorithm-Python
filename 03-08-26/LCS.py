def lcs_length(x, y, m, n):
    
    c = [[0] * (n+1) for _ in range(m+1)]
    b = [[""] * (n+1) for _ in range(m+1)]

    for i in range (1, m+1):
        for j in range (1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = "*"

            elif x[i-1] != y[j-1]:
                if c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = "?"

                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = "#"

    return c, b


def print_lcs(b, x, i, j):
    if i == 0 or j == 0:
        return ""

    if b[i][j] == "*":
        return print_lcs(b, x, i-1, j-1) + x[i-1]
    elif b[i][j] == "?":
        return print_lcs(b, x, i-1, j)
    else:
        return print_lcs(b, x, i, j-1)

x = "BACDB"
y = "BDCB"

m = len(x)
n = len(y)

c, b = lcs_length(x, y, m, n)

print("\n C Table->")
for row in c:
    print(row)

print("\n B Table->")
for row in b:
    print(row)

lcs = print_lcs(b, x, len(x), len(y))
print ("\n Length of the LCS is: ", len(lcs))