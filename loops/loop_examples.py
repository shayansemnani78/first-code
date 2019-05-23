num=12
state=True
a=2
#while a<num :
#    if(num%a==0) :
 #       print("not prime")
##
  #  elif a==num-1 and num%a!=0 :
   #     print("is prime")
    #    break
#
 #   else :
  #      a+=1
while a<num:
    if num%a==0:
        state=False
    else :
        a+=1


if state:
    print("is prime")
else :
    print("not prime")