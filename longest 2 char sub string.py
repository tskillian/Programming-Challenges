#given a string, find the longest sub-string that 
#contains, at most, two characters.

user_input = raw_input('Enter input: ')

best_answer = []
rando = -1

while rando < len(user_input):
	rando += 1
	potential_answer = []

	for letter in list(user_input)[rando:]:
		
		if len(set(potential_answer)) < 2:
			potential_answer.append(letter)
			if len(potential_answer) >= len(best_answer):
				best_answer = potential_answer
		
		elif len(set(potential_answer)) == 2 and letter in potential_answer:
			potential_answer.append(letter)
			if len(potential_answer) >= len(best_answer):
				best_answer = potential_answer
		
		else:
			if len(potential_answer) >= len(best_answer):
				best_answer = potential_answer
			potential_answer = []
		

print "".join(best_answer)

