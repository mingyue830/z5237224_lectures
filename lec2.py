x = 1
print(x)

x = str('abc')
x = 'abc' #short cut

x = str.upper('abc')
print(x) # --> 'ABC' upper func is turn characters into capital. class
y = 'abc'.upper()
print(y) # --> 'ABC' instance

weird_case = 'My fUnNy tYpECASE sTrInG'
# upper first and then lower
weird_case_lower = weird_case.upper().lower()
print(weird_case_lower)

a = True
b = 5
print(f"The value of a is {a} and the value of b is {b}") #more easy for me

lst_a = [1, "string", True, None]
lst_b = ["a", lst_a]
print(lst_a)
print(lst_b)

lst = [1, "string", True, None]
print(f"The item at index 0 is {lst[0]}")
print(f"The item at index 1 is {lst[1]}")
print(f"The item at index 2 is {lst[2]}")
print(f"The item at index 3 is {lst[3]}")

lst = ["a", "b", "c", "d", "e", "f"]
print(f"The slice from index 1 through 4 is {lst[0:2]}" )

lst_a = [1]
list.append(lst_a, 2)
lst_a = [1]
lst_a.append(2) # lst_a is [1, 2]

lst = [1, True, None]
print(f"lst is originally {lst}" )
lst.insert(1, "string") # lst is now [1, "string", True,None]
print(f"After insertion, lst is now {lst}")

lst = [1, "string", True, None, True]
print(f"Original lst is {lst}")
lst.remove(True)
print(f"lst after removing the first True is {lst}")

lst = [1, "string", True, None, True]
no_of_items =len(lst)
print(f"lst has {no_of_items} items")

#tuple use (), can be pack or unpack, it can be sliced
t = ("word", 5, False)

# set can be added and removed
s = {1, 2, 3, 3, 3, 3}


