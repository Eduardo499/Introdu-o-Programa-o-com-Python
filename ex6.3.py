a = [1,1,1,1,2,3,4,5,6]
b = [2,6,5,4,5,3,9,7,2]
c = []

for i in a:
    if i not in c:
        c.append(i)
for j in b:
    if j not in c:
        c.append(j)
        
c.sort()

print(c)
