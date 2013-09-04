#Unit Testing is one of the more basic, but effective, 
#tools for software testing / quality assurance. Your
#job, as an expert test-engineer, is to double-check 
#someone else's test data, and make sure that the 
#expected output is indeed correct. The two functions 
#you are testing is string-reversal and string-to-upper 
#functions.

For each line of input, there are three space-delimited values: the first being the test index (as either 0 or 1), then the test input string, and finally the "expected" output. You must take the test input string, run it through your implementation of the appropriate function based on the test index, and then finally compare it to the "expected" output. If you are confident your code is correct and that the strings match, then the "expected" output is indeed good! Otherwise, the "expected" output is bad (and thus invalid for unit-testing).

tests = raw_input("Enter input: ")
[test_type, test_input, test_result] = tests.split()
print test_input.capitalize()

if int(test_type) == 0:
	if list(test_result) == [x for x in reversed(list(test_input))]:
		print "Test is good!"
	else: 
		print "Test is NO GOOD!"

elif int(test_type) == 1:
	if test_result == test_input.upper():
		print "Test is good!"
	else:
		print "test is NO GOOD!"

else:
	print "Test type should be 0 or 1"
