data = []

for i in range(5):
    data.append(lambda a,i=i*2: i*a)

print(data[4](10))