#Given a well-formed (non-empty, fully valid) string of 
#digits, let the integer N be the sum of digits. Then, 
#given this integer N, turn it into a string of digits. 
#Repeat this process until you only have one digit left. 
#Simple, clean, and easy: focus on writing this as cleanly 
#as possible in your preferred programming language.

user_input = raw_input("Enter digits: ")
sum = user_input

while len(str(user_input)) > 1:
	print user_input
	sum = 0
	for i in str(user_input):
		sum += int(i)
		
	user_input = sum

print user_input
