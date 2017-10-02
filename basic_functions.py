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
def word_counts(file_path, case_sensitive=True, treat_punct_as_word = False, punct = ['!', '.', ',', '"', '?', '~']):
	text = open(file_path, 'r').read()
	if not(case_sensitive):
		text = text.lower()
	# TODO: Add code to count each punctuation character
	# For time being, remove punctuation characters:
	for p in punct:
		text = text.replace(p, ' ')
	words = text.split(' ')
	cleaned_words = []
	for w in words:
		if len(w) > 0:
			cleaned_words.append(w.strip())
	return histogram(cleaned_words)		
	
# Returns the maximum (largest) element in the list.
def my_max(elements):
	if len(elements) > 0:
		curr_max = elements[0]
		for e in elements:
			if e > curr_max:
				curr_max = e
		return curr_max
	return None
	
	# Illustrate variable-length inputs into a funcion
def variable_number_of_inputs(a, b, *rest):
	print("A is " + str(a))
	print("B is " + str(b))
	for e in rest:
		print("  Next Optional Input: " + str(e))
		
# Implement fzip - Zip a set of lists and collapse resulting tuples
# based on an aggregating function f.
def fzip(f, *lists):
	return map(lambda tup: f(*tup), zip(*lists))

def sum_range(a, b):
	if a == b:
		return a
	else:
		return sum_range(a, b - 1) + b

	