names = ["yanis", "ayoub", "mohamed", "quentin"]
marks = [1000, 5, 5000, 2]


for i in range(len(names)):
    if names[i] == "quentin":
        marks[i] += 10000
    print(names[i], "tu as", marks[i], "points")

classroom = {"yanis": 1000, "ayoub": 5, "mohamed": 5000, "quentin": 2}
print(classroom["yanis"])
