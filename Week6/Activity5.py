fibonnaci= lambda x: x if x<=1 else fibonnaci(x-1)+fibonnaci(x-2)

print([fibonnaci(i) for i in range(5)])