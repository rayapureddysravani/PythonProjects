#Lambda function
#Syntax : lambda arguments:expression
x = lambda a:a + 10
print(x(5)) #15

x = lambda x,y:x*y
print(x(5,6)) #30

x = lambda x,y,z:x+y+z
print(x(2,4,8)) #14

#Check even or odd
(lambda num:print("Even") if num%2==0 else print("Odd"))(10)

#Map Function
#syntax :- map(function,iterable)
nums = [10,20,40,50]
sumofnums = list(map(lambda n :n +10,nums))
print(sumofnums) #[20,30,50,60]

#Filter Function
#Syntax :- filter(function,iterable)
nums = (2,7,8,10,5)
even_nums = tuple(filter(lambda n : n%2==0,nums))
print(even_nums) #(2,8,10)

from functools import reduce

#Reduce Function
#Syntax :- Reduce(iterable,func)
nums = [2,8,9,1,6]
sum = reduce(lambda a,b:a+b,nums)
print(sum) #26





