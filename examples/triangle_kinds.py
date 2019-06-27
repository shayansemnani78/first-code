import math
def triangle (h1, h2, h3):
    if h1 + h2 <= h3:
        return False
    elif h1 + h3 <= h2:
        return False
    elif h2 + h3 <= h1:
        return False

    else:
        return True

def triangle_kind (h1, h2, h3):
    if h1 == h2 and h1 == h3:
       print("equiletral")


    elif h1 == h2 or h1 == h3 or h2 == h3:
         if math.sqrt(h1)==math.sqrt(h2)+ math.sqrt(h3) or math.sqrt(h2)==math.sqrt(h1)+ math.sqrt(h3) or math.sqrt(h3)==math.sqrt(h2)+ math.sqrt(h1)

    elif


