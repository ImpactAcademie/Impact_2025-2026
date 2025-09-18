students = ["yanis", "mohamed", "ayoub", "quentin"]
points = [10, 4, 3, 7]

for i in range(len(students)):
    if students[i] == "quentin":
        points[i] = 20
    print(students[i], "a", str(points[i]) + "/20 points !")

classroom = {"yanis": 9, "mohamed": 3, "ayoub": 7}

print(classroom)

s = set([1, 2, 3, 2, 3, 4, 4])
print(s)