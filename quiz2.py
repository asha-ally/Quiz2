def modulus():
	x=[100,110,120,130,140,150] 
	modulus=[number%3 for number in x]
	print(modulus)

def sorted():
	a=['apple','banana','mango']
	b=['avocado','peach','orange']
	c=['pineapple','lemon']
	d=set(a+b+c)
	print(d)
   
def divisible_by_three(n):
	x=range(1,n+1)
	for number in x:
		if number%3==0:
			print(number)



def flatten():
	list = [[1,2],[3,4],[5,6]]
	flatlist=[]
	for sublist in list:
		for item in sublist:
			list.append(flatlist)
			print(flatlist)
	

def smallest(n):
	b=range(1,n)
	print(min(b))

def squares():
	x=dict()
	numbers=range(149,159)
	for number in numbers:
		x[number]=number*number
		print(x)

def greeting():
	 students = [{'age': 19, 'name': 'Eunice'}, {'age': 21, 'name': 'Agnes'}, {'age': 18, 'name': 'Teresa'}, {'age': 22, 'name': 'Asha'}]
	 y.o.b=2019-students['age']
	 msg="Hello {},you were born in{} ".format(students['name'],y.o.b)
