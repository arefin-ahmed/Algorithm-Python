# Activity Selection using Earliest Finish Time 

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

n = int(input("Enter the number of activities: "))

activityID = []
start = []
finish = []

print("\nEnter Activity ID, Start Time and Finish Time:\n")

for i in range(n):

    activityID.append(input("Activity ID: "))
    start.append(int(input("Start Time: ")))
    finish.append(int(input("Finish Time: ")))

    print()

print("\nActivities Before Sorting")
print("Activity\tStart\tFinish")

for i in range(n):
    print(activityID[i], "\t\t", start[i], "\t", finish[i])

# Bubble Sort

for i in range(n - 1):
    for j in range(n - i - 1):

        if finish[j] > finish[j + 1]:

            finish[j], finish[j + 1] = finish[j + 1], finish[j]
            start[j], start[j + 1] = start[j + 1], start[j]
            activityID[j], activityID[j + 1] = activityID[j + 1], activityID[j]

print("\nActivities After Sorting (Earliest Finish Time)")
print("Activity\tStart\tFinish")

for i in range(n):
    print(activityID[i], "\t\t", start[i], "\t", finish[i])

printMaxActivities(activityID, start, finish, n)