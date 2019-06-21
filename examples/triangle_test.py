def triangle (h1, h2, h3):

    if h1+h2 <= h3 :
        return False
    elif h1+h3 <= h2 :
        return False
    elif h2+h3 <= h1 :
        return False
    else :
        return True

a= triangle(1, 1, 2)
print(a)