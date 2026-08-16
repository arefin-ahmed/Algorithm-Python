def greedy_knapsack(profit, weight, capacity, sponsors):
    n = len(profit)

    items = []

    for i in range(n):
        ratio = profit[i] / weight[i]
        items.append([profit[i], weight[i], ratio, sponsors[i]])

    for i in range(n):
        MAX = i

        for j in range(i + 1, n):
            if items[j][2] > items[MAX][2]:
                MAX = j

        if MAX != i:
            items[i], items[MAX] = items[MAX], items[i]

    total_profit = 0
    total_weight = 0
    selected_sponsors = []

    for i in range(n):
        if items[i][1] <= capacity:
            selected_sponsors.append(items[i][3])

            capacity = capacity - items[i][1]

            total_weight = total_weight + items[i][1]

            total_profit = total_profit + items[i][0]

    print("Sponsors After Sorting by Profit/Space Ratio")

    print("Sponsor\tSpace\tOffer\tRatio")

    for i in range(n):
        print(
            items[i][3],
            "\t",
            items[i][1],
            "\t",
            items[i][0],
            "\t",
            round(items[i][2], 2),
        )

    print("\nSelected Sponsors:")

    for sponsor in selected_sponsors:
        print(sponsor, end=" ")

    print()

    print("Total Space Used:", total_weight, "sq.m")

    print("Total Sponsorship:", total_profit)


sponsors = ["S1", "S2", "S3", "S4", "S5", "S6"]

profit = [60000, 100000, 120000, 50000, 70000, 30000]

weight = [10, 20, 15, 8, 12, 5]

capacity = 50


greedy_knapsack(profit, weight, capacity, sponsors)