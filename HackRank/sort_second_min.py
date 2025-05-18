a=[]
c=[]
def myFunc(e):
    return e[1] 
for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append(list((name, score)))
a.sort(key=myFunc)
b=a[1][1]
for x in a:
        if x[1] == b:
            c.append(x[0])
c.sort()
for x in c:
        print(x)