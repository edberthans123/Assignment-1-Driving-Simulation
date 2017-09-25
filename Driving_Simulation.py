Vo = 0
t = int(input("Time: "))
distance = int(input("Distance: "))
speed_limit = 60
a = int(input("Acceleration:"))
v = Vo + a*t
s = Vo*t + 1/2*a*t**2

#v = u + at
#s = ut + 1/2at^2
#s = 1/2t(v + u)
#v^2 = u^2 + 2as

for i in range(0,t+1):
    s = Vo*i + 1/2*a*i**2
    print("Duration" + str(i) + ':' + int(s/10)*'*')
# each (*)=10m

if v > speed_limit:
    print( 'The person went over the speed limit,' + ' Max speed was ' + str(v) + 'm/s')
else:
    print( 'The person did not go over the speed limit,' + ' Max speed was ' + str(v) + 'm/s')

if s >= distance:
    print('The person reached the destination,' + ' Reached' + str(s) + 'm' )
else:
    print('The person did not reached the destination,' + ' Reached' + str(s) + 'm')
