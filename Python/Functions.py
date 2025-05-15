#function creation
def my_func(name):
    print(f"Hii {name}")
my_func("Sravani")

#Number of aruguments
def name(fname , lname):
    print(f"Hii {fname}  {lname}")
name("Sravani","Rayapureddy")

#Arbitary Arguments
def my_func(*kids):
    print("The youngest child is",kids[2])
my_func("Soundarya","Bhopal","Gopal","Sunny")

#Keyword arguments
def my_func(child3,child2,child1):
    print("The youngest child is:",child2)
my_func(child1 = "Ramu",child2="Sita",child3 ="Gita")

#Arbitrary keyword arguments
def my_func(**kid):
    print("your last name is",kid["lname"])
my_func(fname="Sri",lname="Ram")

#Default Parameter value
def my_func(country = "India"):
    print(f"I am from {country} country")
my_func()
my_func("Canada")

#Passing a list as an arguments
def my_func(fruits):
    for fruit in fruits:
        print("Fruit:",fruit)

fruits = ["Apple","Orange","Water melon"]
my_func(fruits)

#Return values
def mul(num):
    return num**2
res = mul(5)
print(res)

#Recursion
def numbers(num):
    if num==0:
        return
    print(num)
    return numbers(num-1) 
numbers(10)

#Factorial of a number using recursion
def fact(n):
    if n == 0 :
        return 1
    else:
        print(numbers)
        return n *fact(n-1)

print("The factorial of a number is",fact(5))