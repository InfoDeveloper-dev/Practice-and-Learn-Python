"""
This program is about storing even numbers from the list
Various Methods will be discussed here
Method 1: Iterating through the loop and applying logic
Method 2: Using Filter Method
"""

even_odd_list = [0,1,2,3,4,5,6]

# Method 1: Iterating through the loop and applying logic
even_elements_list =list()
for each_element in even_odd_list:
	if each_element%2==0:
		even_elements_list.append(each_element)

print("Results from Method 1 is: {}".format(even_elements_list))		

# Method 2: Using Filter Method
def filter_method_even_numbers(function, iterable):
	"""
	Filter takes two argumens named as function and 
	iterable object such as list, dictionary or tuple
	python treats everything as object
	"""
	filtered_even_output = list(filter(function, iterable))
	return filtered_even_output	

# calling Method 2
function = lambda x:x%2==0
result_even_list = filter_method_even_numbers(function=function,
										                          iterable=even_odd_list						
										                         )
print('=' * 37)
print("Result from Method 2 is: {}".format(result_even_list))
