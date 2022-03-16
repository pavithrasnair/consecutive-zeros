string=input("enter a string")
l=[]
k=[]
for i in string:
    if i==str(0):
        l.append(i)
    else:
        k.append(len(l))
        l.clear()
print("count of maximum consecutive zero's:",max(k))