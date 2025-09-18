names = ["ayoub" ,"mohamed" ,"yanis"]
marks = [1000, 5, 500]

for i in range(len(names)):
    if names[i] == "ayoub":
        marks[i] += 100
    print(names[i], "tu as", marks[i], "points")

classroom = {"yanis": "un mec beau gosse", "ayoub": 1000, "mohamed": 500}
print(classroom["yanis"])