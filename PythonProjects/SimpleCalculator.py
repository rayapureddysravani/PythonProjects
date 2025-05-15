def calculator(nunm_1,num_2,opt):
    if(opt == '+'):
        return num_1+num_2
    elif(opt == '-'):
        return num_1-num_2
    elif(opt == '*'):
        return num_1*num_2
    elif(opt == "/"):
        return num_1/num_2
    else:
        return "Invalid operator"
    
num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))
opt   = input("Enter which operation do u want(+,-,*,/) ::")
print(calculator(num_1,num_2,opt))
