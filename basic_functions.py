# These are some examples of python-style function definitions.

# Simple example: Add two numbers
def add_2(x, y):
	return x + y
	
# Illustrate default arguments:
def my_range(start, end, by=1):
	# return range(start, end, by)
	# Homework: rewrite this function to use a for loop rather than resorting to Python's builtin range function.
	rng = []
	next_val = start
	while next_val <= end:
		rng.append(next_val)
		next_val += by
	return rng

# Prints a triangle of the specified length/height n.
# If full == True, n is the height.	
def print_triangle(n, full=False):
	pos = 1
	while pos <= n:
		print('*' * pos)
		pos += 1
	if full:
		pos = n - 1
		while pos >= 1:
			print('*' * pos)
			pos -= 1

# Returns a histogram with item counts.			
def histogram(items):
	d = {}
	for i in items:
		if not(d.has_key(i)):
			d[i] = 0
		d[i] += 1 
	return d
	
# Reads in a file and gets the word counts as a histogram.
def word_counts(file_path, case_sensitive=True):
	return 'Make me do something!'