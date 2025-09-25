maListe = [8,5,7,6,2,4,1]
# def ranger(a):
#     for i in range(0,len(a)):
#         if a(i) > a(i + 1):
#             a.append(i)
def ranger(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if maListe[i]>maListe[j]:
                temp = maListe[i]
                maListe[i]=maListe[j]
                maListe[j]=temp


def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(5))

print(maListe)
ranger(maListe)
print(maListe)