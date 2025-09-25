list1 = [1,3,5,2,9,0,4]

listEnd = [0,1,2,3,4,5,9]
premier = list1[0]
def sorting(list1):
    n=len(list1)
    
    for i in range(n):
        for j in range(i+1,n):
            if list1[i] > list1[j]:
                temp=list1[i]
                list1[i]=list1[j]
                list1[j] = temp
    return list1
print(sorting(list1))

def fibo(n):
    if n<=1:
        return 1
    else: 
        return fibo(n-1)+fibo(n-2)
    

print(fibo(5))