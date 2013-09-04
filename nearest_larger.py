# Write a function, `nearest_larger(arr, i)` which takes an array and an
# index. The function should return another index, `j`: this should
# satisfy:
#
# (a) `arr[i] < arr[j]`, AND
# (b) there is no `j2` closer to `i` than `j` where `arr[i] < arr[j]`.
#
# In case of ties (see example beow), choose the earliest (left-most)
# of the two indices. If no number in `arr` is largr than `arr[i]`,
# return `nil`.

def nearest_larger(arr, i):
	movement = 0
	target = arr[i]
	while movement < max(i, len(arr)-i):
		movement += 1
		if i-movement >= 0 and arr[i-movement] >= target:
			if i-movement >= 0:
				return i-movement
				break
		if i+movement < len(arr) and arr[i+movement] >= target:
			return i+movement
			break
	return 'nil'

