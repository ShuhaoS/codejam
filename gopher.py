#exchange limit 1000
import sys
import math

def fill_area(rec_width, rec_length):
	filled_flag = False
	cell_map = [[False for a in range(rec_length+1)] for b in range(rec_width+1)]
	nearby_occupation = [[0 for a in range(rec_length)] for b in range(rec_width)]
	for i in range(1, 10):
		for x in range(2, rec_width):
			if filled_flag == True:
				break
			for y in range(2, rec_length):
				if filled_flag == True:
					break
				while True:
					if nearby_occupation[x][y] >= i:
						break
					print(str(x) + ' ' + str(y), flush=True)
					prepared_cell = sys.stdin.readline().strip('\n').split(' ')
					cell_x = int(prepared_cell[0])
					cell_y = int(prepared_cell[1])
					if cell_x == -1 and cell_y == -1:
						exit()
					if cell_x == 0 and cell_y == 0:
						filled_flag =  True
						break;
					if cell_map[cell_x][cell_y] == False:
						cell_map[cell_x][cell_y] = True
						for j in range(cell_x-1, cell_x+2):
							for k in range(cell_y-1, cell_y+2):
								if(j>1 and j<rec_width and k>1 and k<rec_length):
									nearby_occupation[j][k] += 1
					else:
						continue



num_of_cases = int(sys.stdin.readline().strip('\n'))
for i in range(num_of_cases):
	rec_area = int(sys.stdin.readline().strip('\n'))
	rec_width = int(math.sqrt(rec_area))
	rec_length = int(math.ceil(rec_area/rec_width))
	fill_area(rec_width, rec_length)