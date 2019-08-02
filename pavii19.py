n1=int(input())
l=[]
flag=1
a1=[]
s1=""
for i in range(2,n1+1):
    for j in range(2,n1+1):
        if i*j==n1:
            l.append(i)
for i in l:
    for j in range(2,i):
        if i%j==0:
            flag=0
            break
        else:
            flag=1
    if flag==1:
        s1=s1+str(i)+" "
print(s1.strip())
