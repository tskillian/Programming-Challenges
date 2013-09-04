#Imagine you are an engineer working on some legacy code that has some odd constraints:
#you're being asked to implement a new function, which basically merges and sorts one 
#list of integers into another list of integers, where you cannot allocate any other 
#structures apart from simple temporary variables (such as an index or counter variable).

#You will be given two lists, list A and B, where the elements are positive integers 
#from 1 to 2147483647; the integer '0' is reserved as "buffer space". List A will 
#not be pre-sorted, though list B will be pre-sorted and will start with a series 
#of '0' values. These '0' values are simply reserved space in list B which is the 
#same number of elements that list A has. You cannot modify list A in any way, 
#though list B is fair game. Your goal is to return a merged and sorted list of 
#elements of list A into list B, where you cannot allocate any extra space other than simple / trivial local variables for your function.

list_a = raw_input("Enter list A: ").split()
list_b = raw_input("Enter list B: ").split()

counter = len(list_a)-1

while counter >= 0:

	for i, z in enumerate(list_b[:]):
		list_b[i] = int(z)
		if int(z) == 0:
			list_b[i] = int(list_a[counter])
			counter -= 1


print sorted(list_b)
