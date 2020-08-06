def my_func(param1= "default"):

	"""
	THIS IS DOCSTRING
	"""

	print("my first python function {}".formet(param1))

	my_func()


	###
	def hello():
		return "hello"

		result = hello()

		print(result)

		####
		def addNum(num1,num2):
			if type(num1)==type(num2)==type(10):
			return num1+num2

		else:
			return "sorry! we need integer"

			result = addNum(2,3)

			print(addNum)





#filter function 

mylist = [1,2,3,4,6,7,8,9]

def even_bool(num):
 return num%2 == 0

 evens = filter(even_bool,mylist)

 ###lambda expression 
 evens = filter(lambda num:num%2 == 0,mylist)

 print(list(evens))	


 ##
 tweet = "Go sports ! #sports"
 result = tweet.split("#")
 print(result)


 ##in operator

 print('x' in [1,2,3])
 #flase

 print('x' in [1,2,3,'x'])
 #true