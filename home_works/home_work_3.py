text=input("enter list with , as a seprator ")
lst = text.split(",")
lst_l=[]
lst_r=[]
number_of_mems=len(lst)
middle=number_of_mems/2
counter=0
while counter < middle:
    lst_l.insert(counter,lst[counter])
    counter+=1

counter_2=int(middle)
while counter_2 < number_of_mems:

    lst_r.insert(counter_2,lst[counter_2])
    counter_2+=1

position_choice=input("pls choose your position with R for right and L for left!!! ")

if position_choice=="R" :
    print(lst_r)
    lst_r.reverse()
    print(lst_r)


elif position_choice=="L" :
    print(lst_l)
    lst_l.reverse()
    print(lst_l)

else :
    print("invalid position")

