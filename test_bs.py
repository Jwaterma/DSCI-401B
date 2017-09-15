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
