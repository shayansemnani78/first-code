text=input("enter list with , as a seprator ")
lst = text.split(",")
lst_l=[]
lst_r=[]
number_of_mems=len(lst)
middle=number_of_mems/2
counter=0
while counter < middle:
    lst_l.insert(counter,lst[counter])
    print(lst_l)
    counter+=1

counter_2=int(middle)
while counter_2 < number_of_mems:
    lst_r.insert(counter_2,lst[middle+1])
    print(lst_r)
    middle+=1
