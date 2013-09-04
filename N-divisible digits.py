#Write a program that takes two integers, N and M, 
#and find the largest integer composed of N-digits 
#that is evenly divisible by M. N will always be 1 
#or greater, with M being 2 or greater. Note that 
#some combinations of N and M will not have a solution.

#Example: if you are given an N of 3 and M of 2, the 
#largest integer with 3-digits is 999, but the 
#largest 3-digit number that is evenly divisible by 
#2 is 998, since 998 Modulo 2 is 0. Another example 
#is where N is 2 and M is 101. Since the largest 
#2-digit integer is 99, and no integers between 1 
#and 99 are divisible by 101, there is no solution.

digits_factor = raw_input("Enter digits and factor: ")
[digits, factor] = digits_factor.split()
minimum = 1

while len(str(minimum)) < int(digits):
	minimum *= 10

answer = (minimum * 10) - 1

while answer >= minimum:
	if answer % int(factor) == 0:
		print answer
		break
	answer -= 1
