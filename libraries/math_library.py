import math
import time

start=time.time()
high_end=10000000
low_end=1
z=0

while low_end<high_end:

    x=1/(low_end**2)
    z=z+x
    low_end+=1


print(math.sqrt(z*6))
print(math.pi)
end=time.time()
print(end-start)