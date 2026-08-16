def printMaxActivities(activityID, start, finish, n):

    count = 1
    i = 0

    print("\nSelected Activities:")
    print("Activity\tStart\tFinish")

    print(activityID[i], "\t\t", start[i], "\t", finish[i])

    for j in range(1, n):
        if start[j] >= finish[i]:
            print(activityID[j], "\t\t", start[j], "\t", finish[j])

            i = j
            count += 1

    print("\nTotal Selected Activities =", count)


def quickSort(activityID, start, finish, lb, ub):

    if lb < ub:
        loc = partition(activityID, start, finish, lb, ub)

        quickSort(activityID, start, finish, lb, loc - 1)

        quickSort(activityID, start, finish, loc + 1, ub)


def partition(activityID, start, finish, lb, ub):

    pivot = finish[lb]

    i = lb + 1
    j = ub

    while i <= j:
        while i <= ub and finish[i] <= pivot:
            i += 1

        while finish[j] > pivot:
            j -= 1

        if i < j:
            finish[i], finish[j] = finish[j], finish[i]

            start[i], start[j] = start[j], start[i]

            activityID[i], activityID[j] = (activityID[j], activityID[i])

    finish[lb], finish[j] = finish[j], finish[lb]

    start[lb], start[j] = start[j], start[lb]

    activityID[lb], activityID[j] = (activityID[j], activityID[lb])

    return j


n = 8

activityID = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]

start = [9.0, 9.5, 10.5, 11.0, 12.0, 13.0, 13.5, 14.5]

finish = [10.5, 11.0, 12.0, 13.0, 13.5, 14.5, 15.0, 16.0]


print("\nActivities After Sorting (Earliest Finish Time)")

print("Activity\tStart\tFinish")

for i in range(n):
    print(activityID[i], "\t\t", start[i], "\t", finish[i])


printMaxActivities(activityID, start, finish, n)
