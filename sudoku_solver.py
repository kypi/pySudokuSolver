
class SudokuPuzzle:
	
	temp_puzzle = []
	def __init__(self,puzzle):
		self.temp_puzzle = puzzle[:]

	def first_blank(self):
		for col in range(0,9):
			for row in range(0,9):
				if(self.temp_puzzle[row][col] == 0):
					return [row,col]
		return [None,None]


	def get_square(self,row,col):
		return int(col/3) + int(row/3)*3

	def get_square_coord(self,square_num):
		return [int(square_num/3)*3, int(square_num%3)*3] # returns [row,col]

	def get_square_coords(self,square_num):
		coords = []

		[start_row,start_col] = self.get_square_coord(square_num)
		for row in range(0,3):
			for col in range(0,3):
				coords.append([start_row + row, start_col + col])
		return coords


	def check_row(self,row_num,value):
		for col in range(0,9):
			if(self.temp_puzzle[row_num][col]==value):
				return False
		return True
	
	def check_col(self,col_num,value):
		for row in range(0,9):
			if(self.temp_puzzle[row][col_num] == value):
				return False
		return True

	def check_square(self,square_num,value):
		for coordinate in self.get_square_coords(square_num):
			if(self.temp_puzzle[coordinate[0]][coordinate[1]] == value):
				return False
		return True

	def check_valid(self,row,col,value):
		return self.check_row(row,value) & self.check_col(col, value) & self.check_square(self.get_square(row,col),value)

# Combine this method with reducing method so that 




# Recursive brute force method
def solve_sudoku(temp_puzzle):
	# Create new puzzle:

	temp_puzzle = SudokuPuzzle(puzzle.temp_puzzle)

	# find first blank:
	[row,col] = temp_puzzle.first_blank()

	# Check if puzzle already complete. if so, return true
	if(row == None):
		print("Puzzle Completed")
		return True
	
	#try each possible value:
	for test_value in range(1,10):
		if(temp_puzzle.check_valid(row,col,test_value)):
			temp_puzzle.temp_puzzle[row][col] = test_value
			if solve_sudoku(temp_puzzle):
				return True
			else:
				temp_puzzle.temp_puzzle[row][col] = 0 #remove false value (for safe backtrack)

	# If got here without returning True, then this path is not true. return false
	return False # Backtrack


puzzle = SudokuPuzzle([ [8,0,0,9,3,0,0,0,2],
						[0,0,9,0,0,0,0,4,0],
						[7,0,2,1,0,0,9,6,0],
						[2,0,0,0,0,0,0,9,0],
						[0,6,0,0,0,0,0,7,0],
						[0,7,0,0,0,6,0,0,5],
						[0,2,7,0,0,8,4,0,6],
						[0,3,0,0,0,0,5,0,0],
						[5,0,0,0,6,2,0,0,8]])

solve_sudoku(puzzle)
print(puzzle.temp_puzzle)