def calc(): 
    while 1:
        num1, num2, func = input("Input Command (ex:1,2,'+') : ") 
        if (func == '+') : 
            ret = add(num1, num2) 
        elif (func == '-') : 
            ret = sub(num1, num2) 
        else : 
            print('Wrong Command!') 
            ret = None 

ret = calc()
if (ret != None):
    print('Result : %d' %ret)

def add(num1, num2):
    return num1 + num2

def sub(num1, num2): 
    return num1 - num2
