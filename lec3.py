a = 0
b = True
if a != 0:
    print("a is non-zero")
elif b is True:
    print("b is True")
elif a < 0 and b is True:
    print("a is negative and b is True")
else:
    print("None of the conditions above hold")



hours = int(40)  #input some numbers
normal_rate: float = 51.45
overload_rate = 88.9
if hours > 35:
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else:
    pay = hours * normal_rate
print(f'{pay}')


numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
temp_largest = None
print('Before', temp_largest)

for number in numbers:
    if temp_largest is None:
        temp_largest = number
    elif number > temp_largest:
        temp_largest = number
    print(number, temp_largest)
print(f'The largest value is {temp_largest}')
