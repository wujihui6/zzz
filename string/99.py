i = 9
while i > 0:
    j = i
    while j > 0:
        print(f"{i}*{j}={i*j}\t",end='')
        j = j-1
    print()
    i = i-1
print()


for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i * j}\t", end='')
    print()


