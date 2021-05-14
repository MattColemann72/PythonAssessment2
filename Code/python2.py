from random import randint, random	
	
	# INSTRUCTIONS

	# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

	# <QUESTION>

	# <EXAMPLES>

	# <HINT>

	# You are allowed access to the internet for this assessment, you can also use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

	# Access Python from you CLI

	# Type help() or for example help(str)



	# <QUESTION 1>    
	
	# Given a string, return a string where for every char in the original string, there are three chars.
    
    # <EXAMPLES>

	# one("The") → "TTThhheee"
	# one("AAbb") → "AAAAAAbbbbbb"
	# one("Hi-There") → "HHHiii---TTThhheeerrreee"

	# <HINT>
	# How does a for loop iterate through a string?

from typing import Counter


def one(input):
	str_input = list(input)
	counter = 3
	i=0
	str_output = ""
	for character in str_input:
		i=0
		while i < counter:
			i += 1
			str_output += character
	return str_output

#print(one("The job"))

#####################################################################################################################

	# <QUESTION 2>

    #  Write a function which returns the boolean True if the input is only divisible by one and itself.
    
    # The function should return the boolean False if not.

	# <EXAMPLES>

    # two(3) → True
    # two(8) → False

	# <HINT>
	# What operator will give you the remainder?
	# Use your CLI to access the Python documentation and get help manipulating strings - help(range).

def two(input):
	if input == 2 or input == 3 or input == 5 or input == 7:
		return True
	elif input % 2 == 0 or input % 3 == 0 or input % 5 == 0 or input % 7 == 0:
		return False
	return True

#print(two(73))

#####################################################################################################################

	# <QUESTION 3>

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

	# So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

	# <EXAMPLES>

	# three(9) → 11106
	# three(5) → 6170

	# <HINT>
	# What happens if you multiply a string by a number?

######################################
# Not sure why this is failing tests #
######################################

def three(a):
	#int_input = int(a)
	str_input = str(a)
	counter = 0
	num_chars = 1
	str_output = ""
	sum_output = 0
	
	while counter <= num_chars:
		if num_chars < 5:
			if counter == num_chars:
				num_chars += 1
				if num_chars != 5:
					str_output += "+"
			else:
				dup_amount = 1
				while dup_amount <= num_chars:
					str_output += str_input
					dup_amount += 1	
				counter += 1
		else:
			break
	int_input = str_output.split("+")
	num1 = int_input[0]
	num2 = int_input[1]
	num3 = int_input[2]
	num4 = int_input[3]
	sum_output = int(num1) + int(num2) + int(num3) + int(num4)
	return f"{str_output} = {str(sum_output)}"

#print(three(9))




#####################################################################################################################

	# <QUESTION 4>

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.
    
    # <EXAMPLES>

	# four("String","Fridge") → "SFtrriidngge"
	# four("Dog","Cat") → "DCoagt"
	# four("True","Tree") → "TTrrueee" 
	# four("return","letter") → "rleettutrenr"

	# <HINT>
	# Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
	# How would you seperate a string into characters?

def four(input1, input2):
	str_input1 = list(input1)
	str_input2 = list(input2)
	counter = len(input1)
	cond = 0
	str_output = ""
	for _char in str_input1:
		if cond < counter:
			_char2 = str_input2[cond]
			str_output += _char + _char2
			cond += 1
	return str_output

# print(four("hello", "BUMPY"))


#####################################################################################################################

	# <QUESTION 5>

	# Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
    
    # <EXAMPLES>
    
    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]
    
	# <HINT>
	# There is a module which can be used to generate random numbers, this module is called random.
	# The random module contains a function called randint.

def five():
	max_num = 5
	random_num = 0
	num = 0
	five_nums = []
	while num < max_num:
		random_num = randint(100,200)
		if random_num % 2 == 0:
			five_nums.append(random_num)
			num += 1
			
	return five_nums
#print(five())

#####################################################################################################################



	# <QUESTION 6>

	# Given a string, return the boolean True if it ends in "py", and False if not. 
	
	# Ignore Case.

	# For Example:

	# six("ilovepy") → True
	# six("welovepy") → True
	# six("welovepyforreal") → False
	# six("pyiscool") → False

	# <HINT>
	# There are no hints for this question.







def six(input):
	str_input = input.lower()
	if str_input.endswith("py"):
		return True
	return False

#print(six("Hankpy"))

#####################################################################################################################

	# <QUESTION 7>

    # Given three ints, a b c, one of them is small, one is medium and one is large. 
	
	# Return the boolean True if the three values are evenly spaced, so the
	# difference between small and medium is the same as the difference between
	# medium and large. 
	
	# Do not assume the ints will come to you in a reasonable order.
    
    # <EXAMPLES>

	# seven(2, 4, 6) → True
	# seven(4, 6, 2) → True
	# seven(4, 6, 3) → False
	# seven(4, 60, 9) → False

	# <HINT>
	# There is a function for lists called sort.
	# Use the cli to access the documentation help(list.sort)

def seven(a, b, c):
	lst_import = [a,b,c]
	lst_import.sort()
	print(lst_import)
	num1 = lst_import[0]
	num2 = lst_import[1]
	num3 = lst_import[2]

	low_mid = num2 - num1
	high_mid = num3 - num2

	if low_mid == high_mid:
		return True
	return False

#seven(12,51,5)



#####################################################################################################################

	# <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.
	
	# The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

	# eight("Hello", 3) → "Ho"
	# eight("Chocolate", 3) → "Choate"
	# eight("Chocolate", 1) → "Choclate"

	# <HINT>
    # Use the cli to access the documentation help(str.replace)




def eight(input,  a):
	str_len = len(input)
	str_out = [input]
	max_takeaway = (str_len / 2) - 0.5
	str.replace(str_out[a], ":(") 

	return str_out

eight("Chocolate", 1)


#####################################################################################################################

	# <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

	# <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

	# <HINT> 
	# There are no hints for this question.

def nine(string1, string2):
    return False

	# <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array. 
	
	# The element value in the i-th row and j-th column of the array should be i*j.

	# <EXAMPLES>

	# ten(3,2) → [[0,0,0],[0,1,2]]
	# ten(2,1) → [[0,0]]
	# ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

	# <HINT>
	# Think about nesting for loops.

def ten(X,Y):
	return []
