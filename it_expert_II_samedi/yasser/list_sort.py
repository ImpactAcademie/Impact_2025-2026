list1=[5,2,4,7,10,1]

list_END=[1,2,4,5,7,10]

def sorting(list1):
    n=len(list1)
    for i in range(n):
        for j in range(i+1,n):
            if list1[i]>list1[j]:
                temp= list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    return list1
print(sorting(list1))

def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

  
print(fibo(5))