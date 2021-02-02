def square(x):
    return x**2
def sum_after_func(func, values):
    return sum([x for x in map(lambda y: func(y), values)])

def sum_after_func_without_sum_func(func, values, result = 0):
    if values:
        result+=func(values[0])
        values.pop(0)
        return sum_after_func_without_sum_func(func, values, result)
    else:
        return result

r = range(4, 6)
#print(sum_after_func_without_sum_func(square, list(r)))

def square_sum(lst):
    if not lst:
        return 0
    else:
        return (square(lst[0]))+(square_sum(lst[1:]))

def square_sum_iterative(lst, result = 0):
    if not lst:
        return result
    return square_sum_iterative(lst[1:], result+lst[0]**2)


#print(square_sum_iterative(r))

class make_couple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def min(self):
        if self.x > self.y:
            return self.y
        return self.x

    def max(self):
        if self.x < self.y:
            return self.y
        return self.x
#x = make_couple(2, 7)
#print(x.min(), x.max())

listt = [1,2,3,4,5,2137]
listt2 = [5, 4, 5, 7, 6, 5]
def scale_by_5(n):
    return n*5
def make_list_scaler(func, lst):
    return [func(x) for x in lst]

def make_list_scaler_no_comp(func, lst, result=[]):
    if not lst:
        return result
    result.append(func(lst[0]))
    return make_list_scaler_no_comp(func, lst[1:], result)
    #return make_list_scaler_no_comp(func, lst.pop(0), result) #  wtf I did not know that poped item is returned !
#print(make_list_scaler_no_comp(scale_by_5, listt))

#  I may assume that lists have the same length
def map_2_electric_boogaloo(func, lst1, lst2):
    return [eval(f"{lst1[x]} {func} {lst2[x]}") for x in range(len(lst1))]

def map_2_electric_boogaloo_no_comp(func, lst1, lst2, result=[]):
    if not lst1:
        return result
    result.append(eval(f"lst1[0] {func} lst2[0]"))
    return map_2_electric_boogaloo_no_comp(func, lst1[1:], lst2[1:], result)

def map_2_electric_boogaloo_map(func, lst1, lst2):
    return map(lambda x, y: eval(f"x {func} y"), lst1, lst2)
#print([x for x in map_2_electric_boogaloo_map("*", listt, listt2)])

def positive(n):
    if n > 0:
        return True
    return False
def all_are(func, lst):
    if not lst:
        return True
    if not func(lst[0]):
        return False
    return all_are(func, lst[1:])
#print(all_are(positive, listt+[-1]))

def repeat_iterative(n, k, result=[]):
    if not k:
        return result
    result.append(n)
    return repeat_iterative(n, k-1, result)
#print(repeat_iterative(4,4))

lyrics = "get a job sha 8 na get a job sha 8 na wah 8 yip sha boom"
lyrics = lyrics.split()
def expand(lyrics, new_lyrics=[], counter=0):
    print(new_lyrics)
    if 2 > len(lyrics):
        return " ".join([l[:-2] for l in new_lyrics]+lyrics)
    if lyrics[0] == lyrics[1]:
        lyrics.pop(0)
        return expand(lyrics, new_lyrics, counter+1)
    
    new_lyrics.append(f"{lyrics[0]} {counter+1}")
    lyrics.pop(0)
    return expand(lyrics, new_lyrics)
#print(expand(lyrics))


lst1 = [1,2,3]
lst2 = [1,2,3]
def make_list_combiner(func, lst1, lst2, result=[]):
    # shouldn't the result be emptied between two separate function calls?
    # So basically default variables are added on function definition.
    # Since list is a mutable, which implies expensive in memory, python doesn't create new result.
    # It reuses the old one, which for some reason still has variables from previous iniciation.
    # This behaviour is similair to the weird stuff I noticed with mutables in JS too.
    if not lst1:
        return result
    print(f"{lst1[0]} {func} {lst2[0]}")
    result.append(eval(f"{lst1[0]} {func} {lst2[0]}"))
    return make_list_combiner(func, lst1[1:], lst2[1:], result)

def make_list_combiner_fixed(func, lst1, lst2, result=None):
    # atomic types will work.
    if result is None:
        result = []
    if not lst1:
        return result
    print(f"{lst1[0]} {func} {lst2[0]}")
    result.append(eval(f"{lst1[0]} {func} {lst2[0]}"))
    return make_list_combiner(func, lst1[1:], lst2[1:], result)


def sum_lsts(lst1, lst2):
    return make_list_combiner("+", lst1, lst2)

def mul_lsts(lst1, lst2):
    return make_list_combiner("*", lst1, lst2)

print(sum_lsts(lst1 ,lst2))
print(mul_lsts(lst1 ,lst2))






