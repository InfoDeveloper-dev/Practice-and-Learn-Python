"""
This program is about storing even numbers from the list
Various Methods will be discussed here
Method 1: Iterating through the loop and applying logic
Method 2: Using Filter Method
Method 3: If the below list is fixed means values does not change \
we can go for method 3
Method 4: Using Map Python Built In Function
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
"""
Method 3
Let us understand this it is called list slicing
list[start:stop:step]
start is 0
stop is end element
step size is 2 which means stepping 1 element
"""
print('=' * 37)
even_values = even_odd_list[0:None:2]
print("Result from method 3 is: {}".format(even_values))
"""
Method 4
Map takes two input
Input 1: Function
Input 2: Iterable Object such as list
"""
def map_function(element):
	try:
		if element%2==0:
			return element
		else: 
			raise Exception("Number {} is not even".format(element))	
	except Exception as message:
		print(message)

evenList = list(map(map_function, even_odd_list))
evenList_filtered =[each for each in evenList if each!=None]
print("Getting all element of Map List is: {}".format(list(evenList_filtered)
						          )
                                                          )
