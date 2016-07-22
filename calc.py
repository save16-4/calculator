def calc(): 
    while 1 :
		num1, num2, func = input("Input Command (ex:1,2,'+') : ")
		if (func == '+') :
			ret = add(num1, num2)
		elif (func == '-') :
			ret = sub(num1, num2)
		elif (func == '*') :
			ret = mul(num1, num2)
		elif (func == '/') :
			ret = div(num1, num2)
		else :
			print('Wrong Command!')
			ret = None
		if (ret != None):
			print('Result : %d' %ret)

def add(num1, num2):
    return num1 + num2

def sub(num1, num2): 
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2
