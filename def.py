def init_array() :
	return [[1 , 2 , 3] , [4, 5, 6] , [7, 8, 9]]

def print_array(array) :
	i = 0
	while  i < len(array) :
		j = 0 
		while j < len(array[i]) :
			print array[i][j]
			j = j + 1
		i = i + 1

print_array(init_array())






