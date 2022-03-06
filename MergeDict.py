# Merge two Python dictionaries into one
a = {'a':1,'b':2}
b = {'c':3,'d':4}

# a.update(b)
# print(a)

for i in b:
    a[i] = b[i]