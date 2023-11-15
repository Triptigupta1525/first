# Importing SequenceMatcher 
# from difflib module 
from difflib import SequenceMatcher 

# Declaring string variables 
string1 = 'I am geek'
string2 = 'I am new geek'

# Using the SequenceMatcher() 
match = SequenceMatcher(None, 
						string1, string2) 

# convert above output into ratio 
# and multiplying it with 100asdsadasdasdasdas
result = match.ratio() * 100

# Display the final result 
print(int(result), "%") 
