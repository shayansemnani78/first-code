def triangle (h1, h2, h3):
     if h1+h2 <= h3:
         return False
     elif h1+h3 <= h2:
         return False
     elif h2+h3 <= h1:
         return False
     else :
         return True

a= triangle(1, 1, 2)
print(a)



def triangle (h1, h2, h3):

    if h1+h2 <= h3 or h1+h3 <= h2 or h2+h3 <= h1:
        return False

    else :
        return True

a= triangle(10, 1, 1)
print(a)
#first code is faster