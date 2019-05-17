a=10
b=20
c=30
d=40
e=35
res=(a<e and e<b) or (c<e and e<d)
print(res)
res_2= (a<e<d) and (not b<e<c)
print(res_2)