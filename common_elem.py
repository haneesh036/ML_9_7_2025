n=int(input("Enter number of elements in list 1:"))
m=int(input("Enter number of elements in list 2:"))
l1=[]
l2=[]
print("Enter elements in list 1:")
for i in range(n):
    a=input()
    l1.append(a)
print("Enter elements in list 2:")    
for j in range(m):
    b=input()
    l2.append(b)
print(l1)
print(l2)
common=[]
for elem in l1 :
    if elem in l2 and elem not in common:
        common.append(elem)
print("common elements:")
print(common)

