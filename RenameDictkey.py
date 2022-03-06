# Renaming key
z = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# z['A']=z.pop('a')
# print(z)


# Get the key of a minimum value from the following dictionary
# mini = min(z.values())
l = list(z.values())
mini = 0
for i in range(0,len(l)):
    if i==0:
        mini=l[i]
    if l[i] < mini:
        mini=l[i]
for k in z:
    if z[k] == mini:
        print(k)

