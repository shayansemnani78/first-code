num = input('enter your array and use , to separate indexes ')
def input_list(lst):
    if lst:
        lst = lst.split(",")
        if len(lst) == 1:
            print(lst)
        else:
            print(lst[::-1])


    else:
        print("None")



input_list(num)