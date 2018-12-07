import sys


def get_min_hack_num(max_damage, rob_prgm):
	num_of_shoots = 0
	num_of_charges = 0
	damage = 0
	shoots = {}
	shoots[0] = 0
	for step in rob_prgm:
		if step == 'C':
			num_of_charges += 1
			shoots[num_of_charges] = 0
		if step == 'S':
			num_of_shoots += 1
			damage += 2 ** num_of_charges
			shoots[num_of_charges] +=  1
	if num_of_shoots > max_damage:
		return 'IMPOSSIBLE'
	min_hack_num = 0
	while True:
		if damage <= max_damage:
			return min_hack_num
		i = len(shoots) - 1
		if shoots[i] == 0:
			del shoots[i]
		else:
			shoots[i] -=1
			shoots[i-1] +=1
			min_hack_num +=1
			damage -= 2 ** (i-1)


num_of_cases = int(sys.stdin.readline().strip('\n'))
for i in range(num_of_cases):
	line = sys.stdin.readline().strip('\n')
	case = line.split(' ')
	max_damage = int(case[0])
	rob_prgm = case[1]
	min_hack_num = get_min_hack_num(max_damage, rob_prgm)
	print('Case #' + str(i+1) + ': ' + str(min_hack_num))

