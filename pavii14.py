n11=int(input())
s11=input()
l=["a","e","i","o","u","A","E","I","O","U"]
f1=""
for i in s11:
	if i not in l:
		f1=f1+i
print(f1[::-1])
