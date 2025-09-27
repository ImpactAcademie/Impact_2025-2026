list1=[4,1,10,87,50,20]

for i in range(5):
    print(i)
    print(list1[i])

max=-100000
for i in list1:
    if i>max:
        max=i

print(max)