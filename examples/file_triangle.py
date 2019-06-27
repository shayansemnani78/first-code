import math


def triangle(h1, h2, h3):
    if h1 + h2 <= h3:
        return False
    elif h1 + h3 <= h2:
        return False
    elif h2 + h3 <= h1:
        return False
    else:
        return True


def triangle_kind(h1, h2, h3):
    mosavi_3=0
    mosavi_2=0
    ghaem_zavie=0
    none_equal=0
    if h1== h2 == h3:
        print("these inputs are motesavi azlae",h1 ,h2 ,h3)
        mosavi_3=+1

    elif h1==h2 or h1==h3 or h3==h1:
         mosavi_2+=1
         print("these inputs are motasavi saghein",h1 ,h2 ,h3)

    elif math.sqrt(h1)== math.sqrt(h2)+math.sqrt(h3) or math.sqrt(h2)== math.sqrt(h1)+math.sqrt(h3) or math.sqrt(h3)== math.sqrt(h1)+math.sqrt(h2)
        print("these inputs are ghaem zavie",h1 ,h2 ,h3)
        ghaem_zavie+=1

    else:
        print("these inputs are mokhtalef azlae",h1 ,h2 ,h3)
        none_equal+=1


if triangle():
    triangle_kind()
    