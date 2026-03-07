data = ['a14','a2','b15','b3','c2','c11']
sorted_data = sorted(data, key = lambda x: (x[0], int(x[1:])))
print(sorted_data)