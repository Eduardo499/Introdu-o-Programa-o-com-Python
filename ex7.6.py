s1 = list('AATTCGAA')
s2 = list('TG')
s3 = list('AC')
s4 = []

s1 = [i for i in s1 if i not in s2]

for i in s3:
    s1.append(i)
s1.sort()

print(''.join(s1))
