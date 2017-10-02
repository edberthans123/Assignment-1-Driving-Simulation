#Program that will transform long variations into short
def name():
    w = input().split('-')
    u = []
    for y in w:
        u.append(y[0])
    print(''.join(u).upper())
name()
