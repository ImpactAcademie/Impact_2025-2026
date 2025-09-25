list1=[5,2,4,7,10,1]

list_end=[]

def srting(list1):
    n=len(list)
    for i in range(n):
        for j in range(i+1,n):
            if list1[i]>list1[j]:
                temp=list1[i]
                list1[i]=list1[j]
                list1[j]=temp



srting(list1)
