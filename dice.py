print "This is a simple dice roll. Input number of sides and dice."

results = []

def dice(sides, dice):
	if sides <= 0 or dice <= 0:
		print "Invalid input."
	else:
		for i in range(0, dice):
			roll = int(random.randint(0, sides))
			results.append(roll)
			
		print results