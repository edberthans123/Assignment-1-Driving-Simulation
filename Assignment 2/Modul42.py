#Input 10 numbers and it will print out number of distinct answers from the input of the modulo 42
a = []
for y in range(0,10):
    y = int(input())
    x = y % 42
    a.append(x)
print(len(set(a)))
