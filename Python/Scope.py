#Local scope
x=300
def my_func():
    x = 100
    return x
res = my_func()
print(res) #100

#Function within Function
def my_func():
    x = 200
    def myinnerfunc():
        print(x)
    myinnerfunc() #200
my_func()

#Global scope
x = 400

def my_func():
    print(x) 
my_func() #400

print(x) #400

#Naming variable
x = 500

def my_func():
    x = 700
    print(x) 
my_func() #700

print(x) #700

#Global Keyword
def my_func():
    global x
    x = 800
    print(x)
my_func() #800

"""Globalkeyword(To change the values of the global variable in local scope using
   with global keyword) """
x = 200

def my_func():
    global x
    x = 300
    print(x)
my_func() #300

print(x) #300

#Nonlocal keyword

def myfunc():
    x = "Hii"
    def myinnerfunc():
        nonlocal x
        x = "Hello"
    myinnerfunc()
    return x
print(myfunc()) #Hello

