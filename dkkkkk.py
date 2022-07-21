print("Hello World")
import math
a = math.cos(math.pi)
b = math.radians(0)
f = math.cos(math.radians(20))
print(a,b,f)

for i in range(21,91):
  c = 15.76*((math.atan(math.radians(55))*math.tan(math.radians(i)))**0.5)
  r = 16/1.45
  d = 11.03*(math.sin(math.radians(i))*f)/(1-(math.cos(math.radians(i-20))))
  aaa = abs(c-d)
  print "--",i,"--"
  print aaa
  
for i in range(21,91):
  x = 23.85*((math.atan(math.radians(46.5))*math.tan(math.radians(i)))**0.5)
  y = 16/1.45
  z = 11.03*(math.sin(math.radians(i))*f)/(1-(math.cos(math.radians(i-20))))
  zzz = abs(z-x)
  print "--",i,"--"
  print zzz