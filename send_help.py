listt = [1,3,4,5]

#print([x*x for x in listt])
#print([x for x in map(lambda x: x*x, listt)])
def my_map(function, listt):
    for x in range(len(listt)):
        listt[x] = function(listt[x])
    return listt
#print(my_map(lambda x: x*x, listt))

#print(listt[::-1])
#print(listt.reverse())
def my_reverse(listt):
    listt2 = listt.copy()
    for i in range(len(listt)):
        listt2[i] = listt[(i*-1)-1]
    return listt2
#print(my_reverse(listt))

#no built in loops allowed
def my_reverse_2_electric_boogaloo(listt):
    
    def my_for(iterator, code_to_execute, from_list, to_list=[]): #  that was tricky af
        if not to_list:
            to_list = from_list.copy()
        code_to_execute(iterator, from_list, to_list)
        if iterator < 0:
            return to_list
        return my_for(iterator-1, code_to_execute, from_list, to_list)

    reverse_function = lambda iterator, f_l, t_l: t_l.__setitem__(iterator, f_l[(iterator*-1)-1]) #  like actually

    res = my_for(iterator=len(listt)-1, code_to_execute=reverse_function, from_list=listt)
    return res

#my_for(iterator=len(listt), fstring=f"list1[{iterator}] = list2[({iterator}*-1)-1]", list1=listt, list2=listt2), then exec() doesnt work because f string is evaluated before running the function
#print(my_reverse_2_electric_boogaloo(listt))

#no built in loops allowed
def merge_sort_with_delete_duplicates(l1, l2, iterator = 0, lastres=[]):

    if not l1:
        return lastres+l2
    if not l2:
        return lastres+l1


    if l1[iterator] == l2[iterator]:
        print(f"{l1[0]} jest rowne {l2[0]}", lastres)
        lastres.append(l1[iterator])
        l1.pop(0)
        l2.pop(0)
        return merge_sort_with_delete_duplicates(l1, l2, 0, lastres)

    if l1[0] < l2[0]:
        print(f"{l1[iterator]} mniejsze od {l2[iterator]}", lastres)
        lastres.append(l1[0])
        l1.pop(0)
        return merge_sort_with_delete_duplicates(l1, l2, 0, lastres)
        
    if l1[0] > l2[0]:
        print(f"{l1[iterator]} wieksze od {l2[iterator]}", lastres)
        lastres.append(l2[iterator])
        l2.pop(0)
        return merge_sort_with_delete_duplicates(l1, l2, 0, lastres)

#  just as in exercise, it works on already sorted lists.
#   print("res",merge_sort_with_delete_duplicates([2,3,5,6,7],[1,2,4,6,8,10]))
list_of_prizes = [
    1, 1,
    2, 2, 2, 2,
    3, 3, 3,
    4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6,
    7, 7, 7, 7,
    8, 8,
    9, 9, 9,
    10, 10, 10, 10, 10, 10, 10, 10, 10
    ]
test_list = [
    5, 3, 1, 1
    ]


def count_combos(prize_list, amount, itere=0):
    print(prize_list, amount)
    if not prize_list:
        return 1
    if amount-prize_list[0] < 0:
        return 0
    return (
        count_combos(prize_list, amount-prize_list[0]) +
        count_combos(prize_list[1:], amount))

def only_one_of_each_kind(prize_list, amount, itere=0):
    if not prize_list:
        return 1
    if amount-prize_list[0] < 0:
        return 0
    return (
        only_one_of_each_kind([x for x in prize_list if x !=prize_list[0]], amount-prize_list[0]) +
        only_one_of_each_kind(prize_list[1:], amount))

def only_one_of_each_kind_with_leftovers(prize_list, amount, itere=0):
    if not prize_list:
        return itere
    if amount-prize_list[0] < 0:
        return 0
    return (
        itere+only_one_of_each_kind_with_leftovers([x for x in prize_list if x !=prize_list[0]], amount-prize_list[0], itere+1) +
        only_one_of_each_kind_with_leftovers(prize_list[1:], amount, itere))


