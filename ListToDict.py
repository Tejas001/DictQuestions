# Convert two lists into a dictionary
a = ['a','b','c']
b = [1,2,3]

d={}

# for k in a:
#     for v in b:
#         d[k] = v
#         b.remove(v)
#         break
# print(d)

for i in range(0,len(a)):
    d[a[i]] = b[i]
    
