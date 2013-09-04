# Write a function, `no_repeats(year_start, year_end)`, which takes a
# range of years and outputs those years which do not have any
# repeated digits.
#
# You should probably write a helper function, `no_repeat?(year)` which
# returns true/false if a singe year doesn't have a repeat.

def is_repeated(year):
    for i in str(year):
        if str(year).count(i) > 1:
            return False
    return True

def no_repeats(year_start, year_end):
    answer = []
    for i in range(year_start, year_end + 1):
        if is_repeated(i) == True:
            answer.append(i)
    return answer
