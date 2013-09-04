# Write a function, `letter_count(str)` that takes a string and
# returns a hash mapping each letter to its frequency. Do not include
# spaces.

def letter_count(user_str):
    results = {}
    for i in user_str:
        if i != " ":
            results[i] = user_str.count(i)
    return results
