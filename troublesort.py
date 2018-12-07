import sys

def get_error_index(list_length, num_list):
	list1 = num_list[::2]
	list2 = num_list[1::2]
	list1.sort()
	list2.sort()
	num_list[::2] = list1
	num_list[1::2] = list2
	for i in range(list_length-1):
		if num_list[i] > num_list[i+1]:
			return i
	return 'OK'

num_of_cases = int(sys.stdin.readline().strip('\n'))
for i in range(num_of_cases):
	list_length = int(sys.stdin.readline().strip('\n'))
	num_list = sys.stdin.readline().strip('\n').split(' ')
	num_list = [int(n) for n in num_list]
	error_index = get_error_index(list_length, num_list)
	print('Case #' + str(i+1) + ': ' + str(error_index))
