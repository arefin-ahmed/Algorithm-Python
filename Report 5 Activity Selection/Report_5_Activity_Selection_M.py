# Activity Selection using Minimum Duration 

def printMaxActivities(activityID, start, finish, duration, n):

    count = 0
    lastFinish = -1

    print("\nSelected Activities:")
    print("Activity\tStart\tFinish\tDuration")

    for i in range(n):

        if start[i] >= lastFinish:

            print(activityID[i], "\t\t", start[i], "\t", finish[i], "\t", duration[i])

            lastFinish = finish[i]
            count += 1

    print("\nTotal Selected Activities =", count)

n = int(input("Enter the number of activities: "))

activityID = []
start = []
finish = []
duration = []

print("\nEnter Activity ID, Start Time and Finish Time:\n")

for i in range(n):
    activityID.append(input("Activity ID: "))
    s = int(input("Start Time: "))
    f = int(input("Finish Time: "))

    start.append(s)
    finish.append(f)
    duration.append(f - s)

    print()

print("\nActivities Before Sorting")
print("Activity\tStart\tFinish\tDuration")

for i in range(n):
    print(activityID[i], "\t\t", start[i], "\t", finish[i], "\t", duration[i])

# Bubble Sort

for i in range(n - 1):
    for j in range(n - i - 1):

        if duration[j] > duration[j + 1]:

            duration[j], duration[j + 1] = duration[j + 1], duration[j]
            start[j], start[j + 1] = start[j + 1], start[j]
            finish[j], finish[j + 1] = finish[j + 1], finish[j]
            activityID[j], activityID[j + 1] = activityID[j + 1], activityID[j]

print("\nActivities After Sorting (Minimum Duration)")
print("Activity\tStart\tFinish\tDuration")

for i in range(n):
    print(activityID[i], "\t\t", start[i], "\t", finish[i], "\t", duration[i])

printMaxActivities(activityID, start, finish, duration, n)