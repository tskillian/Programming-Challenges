# Write a function, `rec_intersection(rect1, rect2)` and returns the
# intersection of the two.
#
# Rectangles are represented as a pair of coordinate-pairs: the
# bottom-left and top-right coordinates (given in `[x, y]` notation).
#
# Hint: You can calculate the left-most x coordinate of the
# intersection by taking the maximum of the left-most x coordinate of
# each rectangle. Likewise, you can calculate the top-most y
# coordinate of the intersection by taking the minimum of the top most
# y coordinate of each rectangle.


def rectangle_intersection(rec1, rec2):
	bot_left1, top_right1 = rec1[0], rec1[1]
	bot_left2, top_right2 = rec2[0], rec2[1]
	left_most = max(bot_left1[0], bot_left2[0])
	right_most = min(top_right1[0], top_right2[0])
	top_most = min(top_right1[1], top_right2[1])
	bot_most = max(bot_left1[1], bot_left2[1])

	if left_most not in range(bot_left2[0], top_right2[0]):
		if top_most not in range(bot_left2[1], top_right2[1]):
			return 'nil'
 
	return [[left_most,bot_most], [ right_most, top_most]]
