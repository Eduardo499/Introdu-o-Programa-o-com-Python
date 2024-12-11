s1 = list('AATTGGAA')
s2 = list('TG')

s1 = [i for i in s1 if i not in s2]

print(''.join(s1))
