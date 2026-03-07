
factorial= lambda x: 1 if x==0 else x*factorial(x-1)

f=factorial(5)

print(f)