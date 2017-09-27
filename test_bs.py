# This is a test driver for our functions defined in basic_functions.py

# Import the module and name as bs
import basic_functions as bs

# Test the add_2 function defined in bs.
print(bs.add_2(3, 5)) 
print(bs.add_2(4, 6)) 
print(bs.add_2(7, 8)) 

# Test the my_range function.
print(bs.my_range(1, 50))
print(bs.my_range(1, 50, 3))
print(bs.my_range(1, 50, by=4)) # Note we can specify the optional arg. inputs
print(bs.my_range(1, 11, by=3))

# Test the triangle-printing function.
bs.print_triangle(3)
print("\n\n")
bs.print_triangle(5)
print("\n\n")
bs.print_triangle(5, full=True)

# Test the histogram function.
print(bs.histogram(['a', 'x', 2, 'x', 3, 2]))

# Test the word_count function.
print(bs.word_counts('./data/sample_text.txt', case_sensitive=False))
print(bs.my_max([2,4,1,9,5])) # Should print 9

print(bs.variable_number_of_inputs(2, 3))
print(bs.variable_number_of_inputs(2, 3, 4, 5, 6, "Something", "Else"))
