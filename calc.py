def main():
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
	# Write code add function

def sub(num1, num2):
	# Write code sub function

def mul(num1, num2):
	# Write code mul function

def div(num1, num2):
	# Write code div function

if __name__ == '__main__':
        main()
