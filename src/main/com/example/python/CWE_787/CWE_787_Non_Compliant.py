x = [100,200,300]
index = int(input())

if index in range(0,len(x)):
    x[index] = 5
    print(x)
else:
    print("Invalid Index!!")