#The McCarthy 91 Function (http://en.wikipedia.org/wiki/McCarthy_91_function) 
#is a recursive function which, given an integer N,
#returns the integer 91 if N is equal to or smaller than 100, or simply
#N-10 if N is greater than 100. Sounds simple, but look at the function 
#definition in the linked Wikipedia article! How could such a function
#work to always return a constant (for N <= 100) that isn't in the 
#function body? Well, that's your task: write out each step that 
#McCarthy's function does for a given integer N.

integer = raw_input('Enter integer: ')

def M(n):
	if n == int(integer):
		print 'M(%i)' %(n)
	if n <= 100:
		print 'M(M(%i)) since %i is equal to or less than 100' %(n+11, n)
		return M(M(n+11))

	else:
		if n == 91:
			print '%i since %i is greater than 100' %(n-10, n)

		else:
			print 'M(%i) since %i is greater than 100' %(n-10, n)
			return n-10

print M(int(integer))
