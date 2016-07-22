def calc(): 
	while 1 :
		num1, num2, func = input("Input Command (ex:1,2,'+') : ")

		if type(num1) is int and type(num2) is int and type(func) is str :		
        		if func is '+' :
        			ret = add(num1, num2)
        		elif func is '-' :
        			ret = sub(num1, num2)
                	elif func is '*' :
                		ret = mul(num1, num2)
                	elif func is '/' :
                		ret = div(num1, num2)
        		else :
        			print('Wrong Command!')
        			ret = None
        		if ret :
        			print('Result : %d' %ret)
        	else :
                        print('Wrong Command!\n')

def add(num1, num2):
    return num1 + num2

def sub(num1, num2): 
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
        if num2 :
            return num1 / num2
        else :
            print("You can't divide with 0!")
            return None
calc()
