# Write a method, `ordered_vowel_words(str)` that takes a string of
# lowercase words and returns a string with just the words containing
# all their vowels (excluding "y") in alphabetical order. Vowels may
# be repeated (`"afoot"` is an ordered vowel word).
#
# You will probably want a helper method, `ordered_vowel_word?(word)`
# which returns true/false if a word's vowels are ordered.

def is_ordered_word(word):
    vowels = list('aeiou')
    spot = -1
    for letter in word:
        if letter in vowels:
            if vowels.index(letter) >= spot:
                spot = vowels.index(letter)
            else:
                return False
    return True

def ordered_voweled_words(input_string):
    answer = []
    words = input_string.split()
    for word in words:
        if is_ordered_word(word) == True:
            answer.append(word)
    return ' '.join(answer)
