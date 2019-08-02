lst = [6, 3, 2, -55, 6, -8, 34, 2]
#     [ 2, 2, 3, 6, 6, -8, 34, -55]
a = lst()
for i in range(lst):
    if i < 0:
        a.append(i)

lst_positive = map(abs, lst)
sorted_lst_positive = sorted(lst_positive)





print (sorted_lst_positive)