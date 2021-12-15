import numpy
path = "input"

call_numbers = numpy.loadtxt(path, max_rows = 1, delimiter=",", dtype=int)
boards = numpy.loadtxt(path, skiprows=1, dtype=int)
total_rows = boards.shape[0]
num_boards = int(total_rows/5)
boards = numpy.reshape(boards, (num_boards,5,5))

called_numbers = []

def check_row(marked_board:numpy.ndarray, mark_index: int):
	offset = int(mark_index / 5) * 5
	row_indices = [column + offset for column in range(5)]
	inverted_row_marks = [not marked_board[i] for i in row_indices]
	if numpy.any(inverted_row_marks):
		return False
	return True

def check_column(marked_board:numpy.ndarray, mark_index: int):
	offset = mark_index % 5
	column_indices = [column*5 + offset for column in range(5)]
	inverted_column_marks = [not marked_board[i] for i in column_indices]
	if numpy.any(inverted_column_marks):
		return False
	return True

def check_winner(board: numpy.ndarray):
	global called_numbers
	marked_board : numpy.ndarray = numpy.in1d(board, called_numbers)
	winning_condition = False
	for mark_index in numpy.where(marked_board==True)[0]:
		if check_row(marked_board, mark_index) or check_column(marked_board, mark_index):
			winning_condition = True
	
	if winning_condition:
		# sum of all unmarked numbers
		unmarked_indices = numpy.where(marked_board!=True)[0]
		sum_unmarked = sum([board[int(i/5)][i%5] for i in unmarked_indices])
		last_called_number = called_numbers[-1]
		return sum_unmarked * last_called_number
	return None

board_indices_in_game = list(range(num_boards))
for number in call_numbers:
	called_numbers.append(number)
	winner_board_indices = []
	for board_index in board_indices_in_game:
		board = boards[board_index]
		result = check_winner(board)
		if type(result) == numpy.int32:
			winner_board_indices.append(board_index)
			if len(board_indices_in_game) == 1:
				print("Last Winning board:")
				print(board)
				print("Marks:")
				print(numpy.in1d(board, call_numbers))
				print("Value is", result)
	for winner_board_index in winner_board_indices:
		board_indices_in_game.remove(winner_board_index)

print("No winner found")