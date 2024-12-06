
#example for recresion

"""def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
if num < 0:
    print("Negative numbers are not allowed.")
elif num == 0:
    print("Factorial is: 1")
else:
    print("Factorial is:", factorial(num))"""



#converting a map object to a list

"""a = [1, 2, 3, 4]
def double(val):
  return val*2

res = list(map(double, a))
print(res)
"""

# example question
"""list =[1,2,3,5]
a=[i*2 for i in list]
print(a)"""

keys =[a,b,c,d]
values = [1,2,3,4]
a = zip(keys,values)
print(list(a))



dict_values = {k:v for {k,v} in zip{key,values}}
print{dict_values}

    

