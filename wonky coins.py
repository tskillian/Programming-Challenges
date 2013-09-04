# Catsylvanian money is a strange thing: they have a coin for every
# denomination (including zero!). A wonky change machine in
# Catsylvania takes any coin of value N and returns 3 new coins,
# valued at N/2, N/3 and N/4 (rounding down).
#
# Write a method `wonky_coins(n)` that returns the number of coins you
# are left with if you take all non-zero coins and keep feeding them
# back into the machine until you are left with only zero-value coins.

def wonky_coins(n):
	coins = [n]
	count = n
	while count > 0:
		count /= 2
		for coin in coins[:]:
			if coin != 0:
				coins.append(coin/2)
				coins.append(coin/3)
				coins.append(coin/4)
				coins.remove(coin)
	return len(coins)
