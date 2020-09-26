#Basic String
a = "Halo"
b = 'hay'

print(a)
print(b)

#Conditions

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

#Loop for/while

for i in range(5):
	print(i)

a = [2,3,4,5,6]
for i in a:
	print(i)
'''
while True:
	print(1)
'''

a = 0
while a < 5:
	print("benar")
	a=a+1

count = 0
while True:
	print("benar")
	count += 1
	if count >= 5:
		break

for x in range(20):
	if x % 2==0:
		continue
	print(x)

#Function

def my_func():
	print("ini adalah fungsi")

my_func()

def my_func2(a):
	print(a)

my_func2(5)

class my_class:
	
	def my_func3():
		print("ini adalah fungsi")

	def my_func4(a):
		print(a)

a = my_class

a.my_func3()
print()
a.my_func4(5)

class my_class_2:
	variable = "Hmm"
	
	def function(self):
		print("Panggil diri sendiri")

b = my_class_2()

print(b.function())




