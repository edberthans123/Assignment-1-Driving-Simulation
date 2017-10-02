cups = [1,0,0]
w = input().upper()
#write a program that determine the last position of the ball is
for i in w:
    if i == 'A':
        cups[0],cups[1] = cups[1],cups[0]
        print(cups)
    elif i == 'B':
        cups[1],cups[2] = cups[2],cups[1]
        print(cups)
    elif i == 'C':
        cups[0],cups[2] = cups[2],cups[0]
        print(cups)
if cups == [1,0,0]:
    print('1')
elif cups == [0,1,0]:
    print('2')
elif cups == [0,0,1]:
    print('3')
else:
    print('it is not here')
