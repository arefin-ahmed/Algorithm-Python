# Activity Selection using Earliest Finish Time


def printMaxActivities(activityID, start, finish, n):

    count = 1
    i = 0

    print("\nSelected Activities:")

    print("Activity\tStart\tFinish")

    print(
        activityID[i],
        "\t\t",
        start[i],
        "\t",
        finish[i]
    )

    for j in range(1, n):

        if start[j] >= finish[i]:

            print(
                activityID[j],
                "\t\t",
                start[j],
                "\t",
                finish[j]
            )

            i = j

            count += 1

    print("\nTotal Selected Activities =", count)


# Input
n = 8

activityID = [
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8"
]

start = [
    9.0,
    9.5,
    10.5,
    11.0,
    12.0,
    13.0,
    13.5,
    14.5
]

finish = [
    10.5,
    11.0,
    12.0,
    13.0,
    13.5,
    14.5,
    15.0,
    16.0
]


print("Activities Before Sorting")

print("Activity\tStart\tFinish")

for i in range(n):

    print(
        activityID[i],
        "\t\t",
        start[i],
        "\t",
        finish[i]
    )


# Bubble Sort by Finish Time
for i in range(n - 1):

    for j in range(n - i - 1):

        if finish[j] > finish[j + 1]:

            finish[j], finish[j + 1] = finish[j + 1], finish[j]

            start[j], start[j + 1] = start[j + 1], start[j]

            activityID[j], activityID[j + 1] = (
                activityID[j + 1],
                activityID[j]
            )


print("\nActivities After Sorting (Earliest Finish Time)")

print("Activity\tStart\tFinish")

for i in range(n):

    print(
        activityID[i],
        "\t\t",
        start[i],
        "\t",
        finish[i]
    )


# Find maximum activities
printMaxActivities(
    activityID,
    start,
    finish,
    n
)