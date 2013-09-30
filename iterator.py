# basics
# print list
for element in [1, 2, 3]:
    print element

# print tuple
for element in (1, 2, 3):
    print element

# print dict
for key in {'one':1, 'two':2}:
    print key

# print string
for char in "123":
    print char

# print lines in readfile
for line in open("text"):
    print line,

# the for statement calls iter() on the container object
# The function returns an iterator object 
# that defines the method next() which accesses elements in the container one at a time

s = 'abc'
it = iter(s)
print it.next() # a
print it.next() # b
print it.next() # c
# print it.next() -> raise StopIteration

# so you can add iterator behavior to your classes
class waitingLine(object):
	"""waitingLine"""
	def __init__(self, line):
		self.line= line

	# __iter__ returns an object with a next() method
	def __iter__(self):
		return self

	# next method
	def next(self):
		if len(self.line) == 0:
			raise StopIteration
		return self.line.pop()

# init a waitingLine
line= waitingLine(['john', 'marry', 'larry'])
for person in line:
	print person


# Generator
# hey are written like regular functions 
# but use the yield statement whenever they want to return data
def counts():
	for index in range(10):
		yield index

for count in counts():
	print count

# List Comprehensions
squares = [x**2 for x in range(10)]
print squares

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print [weapon.strip() for weapon in freshfruit]

# Generator Expressions
# expressions using a syntax similar to list comprehensions 
# but with parentheses instead of brackets
print sum(i*i for i in range(10))


# dict comprehensions
# create dictionaries from arbitrary key and value expressions:
print {x: x**2 for x in (2, 4, 6)}
