def lcs_length(x, y):
    m = len(x)
    n = len(y)

    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[""] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "*"

            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "?"

            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "#"

    return c, b


def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return ""

    if b[i][j] == "*":
        return print_lcs(b, X, i - 1, j - 1) + X[i - 1]

    elif b[i][j] == "?":
        return print_lcs(b, X, i - 1, j)

    else:
        return print_lcs(b, X, i, j - 1)

x = input ("First input -> ")
y = input ("Second input -> ")

c, b = lcs_length(x, y)

print("Length Table (c):")
for row in c:
    print(row)

print("\nDirection Table (b):")
for row in b:
    print(row)

lcs = print_lcs(b, x, len(x), len(y))

print("\nLongest Common Subsequence:", lcs)
print("Length of LCS:", len(lcs))