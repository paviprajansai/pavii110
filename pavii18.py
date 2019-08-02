n1=int(input())
l=[]
c1=0
k1="kabali"
a1=sorted(k1)
for i in range(n1):
	s1=input()
	l.append(s1)
for i in l:
	if sorted(i)==a1:
		c1=c1+1
print(c1)
